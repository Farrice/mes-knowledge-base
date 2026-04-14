# warproxxx/poly-maker Source Material
## Fetched: 2026-04-13
## Repository: https://github.com/warproxxx/poly-maker

### Repository Structure
```
.env.example
.gitignore
.python-version
LICENSE
README.md
data_updater/erc20ABI.json
data_updater/find_markets.py
data_updater/google_utils.py
data_updater/trading_utils.py
main.py
poly_data/CONSTANTS.py
poly_data/__init__.py
poly_data/abis.py
poly_data/data_processing.py
poly_data/data_utils.py
poly_data/global_state.py
poly_data/polymarket_client.py
poly_data/trading_utils.py
poly_data/utils.py
poly_data/websocket_handlers.py
poly_merger/README.md
poly_merger/merge.js
poly_merger/package-lock.json
poly_merger/package.json
poly_merger/safe-helpers.js
poly_merger/safeAbi.js
poly_stats/__init__.py
poly_stats/account_stats.py
poly_utils/__init__.py
poly_utils/google_utils.py
pyproject.toml
trading.py
update_markets.py
update_stats.py
uv.lock
```

---

### File: .env.example
```
# Polymarket Authentication
PK=your_private_key_here
BROWSER_ADDRESS=your_wallet_address_here

# Google Sheets (for data_updater)
SPREADSHEET_URL=https://docs.google.com/spreadsheets/d/1Kt6yGY7CZpB75cLJJAdWo7LSp9Oz7pjqfuVWgtn7Ns/edit?gid=97507557#gid=97507557
#replace with YOUR url
```

### File: pyproject.toml
```toml
[project]
name = "poly-maker"
version = "0.1.0"
description = "A market making bot for Polymarket prediction markets"
readme = "README.md"
requires-python = ">=3.9.10"
license = { text = "MIT" }

dependencies = [
    "py-clob-client==0.28.0",
    "python-dotenv==1.2.1",
    "pandas==2.3.3",
    "gspread==6.2.1",
    "gspread-dataframe==4.0.0",
    "sortedcontainers==2.4.0",
    "eth-account==0.13.7",
    "eth-utils==5.3.1",
    "poly_eip712_structs==0.0.1",
    "py_order_utils==0.3.2",
    "requests==2.32.5",
    "websockets==15.0.1",
    "cryptography==46.0.3",
    "google-auth==2.42.1",
    "web3==7.14.0",
]

[project.optional-dependencies]
dev = [
    "black==24.4.2",
    "pytest==8.2.2",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["poly_data", "poly_stats", "poly_utils", "data_updater"]

[tool.black]
line-length = 100
target-version = ["py39"]
```

### File: main.py
```python
import gc
import time
import asyncio
import traceback
import threading

from poly_data.polymarket_client import PolymarketClient
from poly_data.data_utils import update_markets, update_positions, update_orders
from poly_data.websocket_handlers import connect_market_websocket, connect_user_websocket
import poly_data.global_state as global_state
from poly_data.data_processing import remove_from_performing
from dotenv import load_dotenv

load_dotenv()

def update_once():
    """
    Initialize the application state by fetching market data, positions, and orders.
    """
    update_markets()
    update_positions()
    update_orders()

def remove_from_pending():
    """
    Clean up stale trades that have been pending for too long (>15 seconds).
    """
    try:
        current_time = time.time()
        for col in list(global_state.performing.keys()):
            for trade_id in list(global_state.performing[col]):
                try:
                    if current_time - global_state.performing_timestamps[col].get(trade_id, current_time) > 15:
                        print(f"Removing stale entry {trade_id} from {col} after 15 seconds")
                        remove_from_performing(col, trade_id)
                        print("After removing: ", global_state.performing, global_state.performing_timestamps)
                except:
                    print("Error in remove_from_pending")
                    print(traceback.format_exc())
    except:
        print("Error in remove_from_pending")
        print(traceback.format_exc())

def update_periodically():
    """
    Background thread: positions/orders every 5s, markets every 30s.
    """
    i = 1
    while True:
        time.sleep(5)
        try:
            remove_from_pending()
            update_positions(avgOnly=True)
            update_orders()
            if i % 6 == 0:
                update_markets()
                i = 1
            gc.collect()
            i += 1
        except:
            print("Error in update_periodically")
            print(traceback.format_exc())

async def main():
    global_state.client = PolymarketClient()
    global_state.all_tokens = []
    update_once()
    print("After initial updates: ", global_state.orders, global_state.positions)
    print("\n")
    print(f'There are {len(global_state.df)} market, {len(global_state.positions)} positions and {len(global_state.orders)} orders. Starting positions: {global_state.positions}')

    update_thread = threading.Thread(target=update_periodically, daemon=True)
    update_thread.start()

    while True:
        try:
            await asyncio.gather(
                connect_market_websocket(global_state.all_tokens),
                connect_user_websocket()
            )
            print("Reconnecting to the websocket")
        except:
            print("Error in main loop")
            print(traceback.format_exc())
        await asyncio.sleep(1)
        gc.collect()

if __name__ == "__main__":
    asyncio.run(main())
```

### File: trading.py
```python
import gc
import os
import json
import asyncio
import traceback
import pandas as pd
import math

import poly_data.global_state as global_state
import poly_data.CONSTANTS as CONSTANTS

from poly_data.trading_utils import get_best_bid_ask_deets, get_order_prices, get_buy_sell_amount, round_down, round_up
from poly_data.data_utils import get_position, get_order, set_position

if not os.path.exists('positions/'):
    os.makedirs('positions/')

def send_buy_order(order):
    client = global_state.client
    existing_buy_size = order['orders']['buy']['size']
    existing_buy_price = order['orders']['buy']['price']

    price_diff = abs(existing_buy_price - order['price']) if existing_buy_price > 0 else float('inf')
    size_diff = abs(existing_buy_size - order['size']) if existing_buy_size > 0 else float('inf')

    should_cancel = (
        price_diff > 0.005 or
        size_diff > order['size'] * 0.1 or
        existing_buy_size == 0
    )

    if should_cancel and (existing_buy_size > 0 or order['orders']['sell']['size'] > 0):
        print(f"Cancelling buy orders - price diff: {price_diff:.4f}, size diff: {size_diff:.1f}")
        client.cancel_all_asset(order['token'])
    elif not should_cancel:
        print(f"Keeping existing buy orders - minor changes: price diff: {price_diff:.4f}, size diff: {size_diff:.1f}")
        return

    incentive_start = order['mid_price'] - order['max_spread']/100
    trade = True

    if order['price'] < incentive_start:
        trade = False

    if trade:
        if order['price'] >= 0.1 and order['price'] < 0.9:
            print(f'Creating new order for {order["size"]} at {order["price"]}')
            print(order['token'], 'BUY', order['price'], order['size'])
            client.create_order(
                order['token'],
                'BUY',
                order['price'],
                order['size'],
                True if order['neg_risk'] == 'TRUE' else False
            )
        else:
            print("Not creating buy order because its outside acceptable price range (0.1-0.9)")
    else:
        print(f'Not creating new order because order price of {order["price"]} is less than incentive start price of {incentive_start}. Mid price is {order["mid_price"]}')


def send_sell_order(order):
    client = global_state.client
    existing_sell_size = order['orders']['sell']['size']
    existing_sell_price = order['orders']['sell']['price']

    price_diff = abs(existing_sell_price - order['price']) if existing_sell_price > 0 else float('inf')
    size_diff = abs(existing_sell_size - order['size']) if existing_sell_size > 0 else float('inf')

    should_cancel = (
        price_diff > 0.005 or
        size_diff > order['size'] * 0.1 or
        existing_sell_size == 0
    )

    if should_cancel and (existing_sell_size > 0 or order['orders']['buy']['size'] > 0):
        print(f"Cancelling sell orders - price diff: {price_diff:.4f}, size diff: {size_diff:.1f}")
        client.cancel_all_asset(order['token'])
    elif not should_cancel:
        print(f"Keeping existing sell orders - minor changes: price diff: {price_diff:.4f}, size diff: {size_diff:.1f}")
        return

    print(f'Creating new order for {order["size"]} at {order["price"]}')
    client.create_order(
        order['token'],
        'SELL',
        order['price'],
        order['size'],
        True if order['neg_risk'] == 'TRUE' else False
    )

market_locks = {}

async def perform_trade(market):
    if market not in market_locks:
        market_locks[market] = asyncio.Lock()

    async with market_locks[market]:
        try:
            client = global_state.client
            row = global_state.df[global_state.df['condition_id'] == market].iloc[0]
            round_length = len(str(row['tick_size']).split(".")[1])
            params = global_state.params[row['param_type']]

            deets = [
                {'name': 'token1', 'token': row['token1'], 'answer': row['answer1']},
                {'name': 'token2', 'token': row['token2'], 'answer': row['answer2']}
            ]
            print(f"\n\n{pd.Timestamp.utcnow().tz_localize(None)}: {row['question']}")

            pos_1 = get_position(row['token1'])['size']
            pos_2 = get_position(row['token2'])['size']

            # POSITION MERGING LOGIC
            amount_to_merge = min(pos_1, pos_2)
            if float(amount_to_merge) > CONSTANTS.MIN_MERGE_SIZE:
                pos_1 = client.get_position(row['token1'])[0]
                pos_2 = client.get_position(row['token2'])[0]
                amount_to_merge = min(pos_1, pos_2)
                scaled_amt = amount_to_merge / 10**6

                if scaled_amt > CONSTANTS.MIN_MERGE_SIZE:
                    print(f"Position 1 is of size {pos_1} and Position 2 is of size {pos_2}. Merging positions")
                    client.merge_positions(amount_to_merge, market, row['neg_risk'] == 'TRUE')
                    set_position(row['token1'], 'SELL', scaled_amt, 0, 'merge')
                    set_position(row['token2'], 'SELL', scaled_amt, 0, 'merge')

            # TRADING LOGIC FOR EACH OUTCOME
            for detail in deets:
                token = int(detail['token'])
                orders = get_order(token)
                deets = get_best_bid_ask_deets(market, detail['name'], 100, 0.1)

                if deets['best_bid'] is None or deets['best_ask'] is None or deets['best_bid_size'] is None or deets['best_ask_size'] is None:
                    deets = get_best_bid_ask_deets(market, detail['name'], 20, 0.1)

                best_bid = deets['best_bid']
                best_bid_size = deets['best_bid_size']
                second_best_bid = deets['second_best_bid']
                second_best_bid_size = deets['second_best_bid_size']
                top_bid = deets['top_bid']
                best_ask = deets['best_ask']
                best_ask_size = deets['best_ask_size']
                second_best_ask = deets['second_best_ask']
                second_best_ask_size = deets['second_best_ask_size']
                top_ask = deets['top_ask']

                best_bid = round(best_bid, round_length)
                best_ask = round(best_ask, round_length)

                try:
                    overall_ratio = (deets['bid_sum_within_n_percent']) / (deets['ask_sum_within_n_percent'])
                except:
                    overall_ratio = 0

                try:
                    second_best_bid = round(second_best_bid, round_length)
                    second_best_ask = round(second_best_ask, round_length)
                except:
                    pass

                top_bid = round(top_bid, round_length)
                top_ask = round(top_ask, round_length)

                pos = get_position(token)
                position = pos['size']
                avgPrice = pos['avgPrice']
                position = round_down(position, 2)

                bid_price, ask_price = get_order_prices(
                    best_bid, best_bid_size, top_bid, best_ask,
                    best_ask_size, top_ask, avgPrice, row
                )

                bid_price = round(bid_price, round_length)
                ask_price = round(ask_price, round_length)
                mid_price = (top_bid + top_ask) / 2

                print(f"\nFor {detail['answer']}. Orders: {orders} Position: {position}, "
                      f"avgPrice: {avgPrice}, Best Bid: {best_bid}, Best Ask: {best_ask}, "
                      f"Bid Price: {bid_price}, Ask Price: {ask_price}, Mid Price: {mid_price}")

                other_token = global_state.REVERSE_TOKENS[str(token)]
                other_position = get_position(other_token)['size']

                buy_amount, sell_amount = get_buy_sell_amount(position, bid_price, row, other_position)
                max_size = row.get('max_size', row['trade_size'])

                order = {
                    "token": token,
                    "mid_price": mid_price,
                    "neg_risk": row['neg_risk'],
                    "max_spread": row['max_spread'],
                    'orders': orders,
                    'token_name': detail['name'],
                    'row': row
                }

                print(f"Position: {position}, Other Position: {other_position}, "
                      f"Trade Size: {row['trade_size']}, Max Size: {max_size}, "
                      f"buy_amount: {buy_amount}, sell_amount: {sell_amount}")

                fname = 'positions/' + str(market) + '.json'

                # SELL ORDER LOGIC
                if sell_amount > 0:
                    if avgPrice == 0:
                        print("Avg Price is 0. Skipping")
                        continue

                    order['size'] = sell_amount
                    order['price'] = ask_price

                    n_deets = get_best_bid_ask_deets(market, detail['name'], 100, 0.1)
                    mid_price = round_up((n_deets['best_bid'] + n_deets['best_ask']) / 2, round_length)
                    spread = round(n_deets['best_ask'] - n_deets['best_bid'], 2)
                    pnl = (mid_price - avgPrice) / avgPrice * 100

                    print(f"Mid Price: {mid_price}, Spread: {spread}, PnL: {pnl}")

                    risk_details = {
                        'time': str(pd.Timestamp.utcnow().tz_localize(None)),
                        'question': row['question']
                    }

                    try:
                        ratio = (n_deets['bid_sum_within_n_percent']) / (n_deets['ask_sum_within_n_percent'])
                    except:
                        ratio = 0

                    pos_to_sell = sell_amount

                    # STOP-LOSS LOGIC
                    if (pnl < params['stop_loss_threshold'] and spread <= params['spread_threshold']) or row['3_hour'] > params['volatility_threshold']:
                        risk_details['msg'] = (f"Selling {pos_to_sell} because spread is {spread} and pnl is {pnl} "
                                              f"and ratio is {ratio} and 3 hour volatility is {row['3_hour']}")
                        print("Stop loss Triggered: ", risk_details['msg'])

                        order['size'] = pos_to_sell
                        order['price'] = n_deets['best_bid']

                        risk_details['sleep_till'] = str(pd.Timestamp.utcnow().tz_localize(None) +
                                                        pd.Timedelta(hours=params['sleep_period']))

                        print("Risking off")
                        send_sell_order(order)
                        client.cancel_all_market(market)

                        open(fname, 'w').write(json.dumps(risk_details))
                        continue

                # BUY ORDER LOGIC
                max_size = row.get('max_size', row['trade_size'])

                if position < max_size and position < 250 and buy_amount > 0 and buy_amount >= row['min_size']:
                    sheet_value = row['best_bid']
                    if detail['name'] == 'token2':
                        sheet_value = 1 - row['best_ask']
                    sheet_value = round(sheet_value, round_length)
                    order['size'] = buy_amount
                    order['price'] = bid_price
                    price_change = abs(order['price'] - sheet_value)

                    send_buy = True

                    # RISK-OFF PERIOD CHECK
                    if os.path.isfile(fname):
                        risk_details = json.load(open(fname))
                        start_trading_at = pd.to_datetime(risk_details['sleep_till'])
                        current_time = pd.Timestamp.utcnow().tz_localize(None)
                        print(risk_details, current_time, start_trading_at)
                        if current_time < start_trading_at:
                            send_buy = False
                            print(f"Not sending a buy order because recently risked off. "
                                 f"Risked off at {risk_details['time']}")

                    if send_buy:
                        if row['3_hour'] > params['volatility_threshold'] or price_change >= 0.05:
                            print(f'3 Hour Volatility of {row["3_hour"]} is greater than max volatility of '
                                  f'{params["volatility_threshold"]} or price of {order["price"]} is outside '
                                  f'0.05 of {sheet_value}. Cancelling all orders')
                            client.cancel_all_asset(order['token'])
                        else:
                            rev_token = global_state.REVERSE_TOKENS[str(token)]
                            rev_pos = get_position(rev_token)
                            if rev_pos['size'] > row['min_size']:
                                print("Bypassing creation of new buy order because there is a reverse position")
                                if orders['buy']['size'] > CONSTANTS.MIN_MERGE_SIZE:
                                    print("Cancelling buy orders because there is a reverse position")
                                    client.cancel_all_asset(order['token'])
                                continue

                            if overall_ratio < 0:
                                send_buy = False
                                print(f"Not sending a buy order because overall ratio is {overall_ratio}")
                                client.cancel_all_asset(order['token'])
                            else:
                                if best_bid > orders['buy']['price']:
                                    print(f"Sending Buy Order for {token} because better price. "
                                          f"Orders look like this: {orders['buy']}. Best Bid: {best_bid}")
                                    send_buy_order(order)
                                elif position + orders['buy']['size'] < 0.95 * max_size:
                                    print(f"Sending Buy Order for {token} because not enough position + size")
                                    send_buy_order(order)
                                elif orders['buy']['size'] > order['size'] * 1.01:
                                    print(f"Resending buy orders because open orders are too large")
                                    send_buy_order(order)

                # TAKE PROFIT / SELL ORDER MANAGEMENT
                elif sell_amount > 0:
                    order['size'] = sell_amount
                    tp_price = round_up(avgPrice + (avgPrice * params['take_profit_threshold']/100), round_length)
                    order['price'] = round_up(tp_price if ask_price < tp_price else ask_price, round_length)

                    tp_price = float(tp_price)
                    order_price = float(orders['sell']['price'])
                    diff = abs(order_price - tp_price)/tp_price * 100

                    if diff > 2:
                        print(f"Sending Sell Order for {token} because better current order price of "
                              f"{order_price} is deviant from the tp_price of {tp_price} and diff is {diff}")
                        send_sell_order(order)
                    elif orders['sell']['size'] < position * 0.97:
                        print(f"Sending Sell Order for {token} because not enough sell size. "
                              f"Position: {position}, Sell Size: {orders['sell']['size']}")
                        send_sell_order(order)

        except Exception as ex:
            print(f"Error performing trade for {market}: {ex}")
            traceback.print_exc()

        gc.collect()
        await asyncio.sleep(2)
```

### File: poly_data/polymarket_client.py
```python
from dotenv import load_dotenv
import os

from py_clob_client.client import ClobClient
from py_clob_client.clob_types import OrderArgs, BalanceAllowanceParams, AssetType, PartialCreateOrderOptions
from py_clob_client.constants import POLYGON

from web3 import Web3
from web3.middleware import ExtraDataToPOAMiddleware
from eth_account import Account

import requests
import pandas as pd
import json
import subprocess

from py_clob_client.clob_types import OpenOrderParams
from poly_data.abis import NegRiskAdapterABI, ConditionalTokenABI, erc20_abi

load_dotenv()


class PolymarketClient:
    def __init__(self, pk='default') -> None:
        host="https://clob.polymarket.com"
        key=os.getenv("PK")
        browser_address = os.getenv("BROWSER_ADDRESS")

        print("Initializing Polymarket client...")
        chain_id=POLYGON
        self.browser_wallet=Web3.to_checksum_address(browser_address)

        self.client = ClobClient(
            host=host,
            key=key,
            chain_id=chain_id,
            funder=self.browser_wallet,
            signature_type=2
        )

        self.creds = self.client.create_or_derive_api_creds()
        self.client.set_api_creds(creds=self.creds)

        web3 = Web3(Web3.HTTPProvider("https://polygon-rpc.com"))
        web3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)

        self.usdc_contract = web3.eth.contract(
            address="0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
            abi=erc20_abi
        )

        self.addresses = {
            'neg_risk_adapter': '0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296',
            'collateral': '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174',
            'conditional_tokens': '0x4D97DCd97eC945f40cF65F87097ACe5EA0476045'
        }

        self.neg_risk_adapter = web3.eth.contract(
            address=self.addresses['neg_risk_adapter'],
            abi=NegRiskAdapterABI
        )

        self.conditional_tokens = web3.eth.contract(
            address=self.addresses['conditional_tokens'],
            abi=ConditionalTokenABI
        )

        self.web3 = web3

    def create_order(self, marketId, action, price, size, neg_risk=False):
        order_args = OrderArgs(
            token_id=str(marketId),
            price=price,
            size=size,
            side=action
        )

        signed_order = None
        if neg_risk == False:
            signed_order = self.client.create_order(order_args)
        else:
            signed_order = self.client.create_order(order_args, options=PartialCreateOrderOptions(neg_risk=True))

        try:
            resp = self.client.post_order(signed_order)
            return resp
        except Exception as ex:
            print(ex)
            return {}

    def get_order_book(self, market):
        orderBook = self.client.get_order_book(market)
        return pd.DataFrame(orderBook.bids).astype(float), pd.DataFrame(orderBook.asks).astype(float)

    def get_usdc_balance(self):
        return self.usdc_contract.functions.balanceOf(self.browser_wallet).call() / 10**6

    def get_pos_balance(self):
        res = requests.get(f'https://data-api.polymarket.com/value?user={self.browser_wallet}')
        return float(res.json()['value'])

    def get_total_balance(self):
        return self.get_usdc_balance() + self.get_pos_balance()

    def get_all_positions(self):
        res = requests.get(f'https://data-api.polymarket.com/positions?user={self.browser_wallet}')
        return pd.DataFrame(res.json())

    def get_raw_position(self, tokenId):
        return int(self.conditional_tokens.functions.balanceOf(self.browser_wallet, int(tokenId)).call())

    def get_position(self, tokenId):
        raw_position = self.get_raw_position(tokenId)
        shares = float(raw_position / 1e6)
        if shares < 1:
            shares = 0
        return raw_position, shares

    def get_all_orders(self):
        orders_df = pd.DataFrame(self.client.get_orders())
        for col in ['original_size', 'size_matched', 'price']:
            if col in orders_df.columns:
                orders_df[col] = orders_df[col].astype(float)
        return orders_df

    def get_market_orders(self, market):
        orders_df = pd.DataFrame(self.client.get_orders(OpenOrderParams(
            market=market,
        )))
        for col in ['original_size', 'size_matched', 'price']:
            if col in orders_df.columns:
                orders_df[col] = orders_df[col].astype(float)
        return orders_df

    def cancel_all_asset(self, asset_id):
        self.client.cancel_market_orders(asset_id=str(asset_id))

    def cancel_all_market(self, marketId):
        self.client.cancel_market_orders(market=marketId)

    def merge_positions(self, amount_to_merge, condition_id, is_neg_risk_market):
        amount_to_merge_str = str(amount_to_merge)
        node_command = f'node poly_merger/merge.js {amount_to_merge_str} {condition_id} {"true" if is_neg_risk_market else "false"}'
        print(node_command)
        result = subprocess.run(node_command, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print("Error:", result.stderr)
            raise Exception(f"Error in merging positions: {result.stderr}")
        print("Done merging")
        return result.stdout
```

### File: poly_data/websocket_handlers.py
```python
import asyncio
import json
import websockets
import traceback

from poly_data.data_processing import process_data, process_user_data
import poly_data.global_state as global_state

async def connect_market_websocket(chunk):
    uri = "wss://ws-subscriptions-clob.polymarket.com/ws/market"
    async with websockets.connect(uri, ping_interval=5, ping_timeout=None) as websocket:
        message = {"assets_ids": chunk}
        await websocket.send(json.dumps(message))

        print("\n")
        print(f"Sent market subscription message: {message}")

        try:
            while True:
                message = await websocket.recv()
                json_data = json.loads(message)
                process_data(json_data)
        except websockets.ConnectionClosed:
            print("Connection closed in market websocket")
            print(traceback.format_exc())
        except Exception as e:
            print(f"Exception in market websocket: {e}")
            print(traceback.format_exc())
        finally:
            await asyncio.sleep(5)

async def connect_user_websocket():
    uri = "wss://ws-subscriptions-clob.polymarket.com/ws/user"

    async with websockets.connect(uri, ping_interval=5, ping_timeout=None) as websocket:
        message = {
            "type": "user",
            "auth": {
                "apiKey": global_state.client.client.creds.api_key,
                "secret": global_state.client.client.creds.api_secret,
                "passphrase": global_state.client.client.creds.api_passphrase
            }
        }

        await websocket.send(json.dumps(message))

        print("\n")
        print(f"Sent user subscription message")

        try:
            while True:
                message = await websocket.recv()
                json_data = json.loads(message)
                process_user_data(json_data)
        except websockets.ConnectionClosed:
            print("Connection closed in user websocket")
            print(traceback.format_exc())
        except Exception as e:
            print(f"Exception in user websocket: {e}")
            print(traceback.format_exc())
        finally:
            await asyncio.sleep(5)
```

### File: poly_data/trading_utils.py
```python
import math
from poly_data.data_utils import update_positions
import poly_data.global_state as global_state

def get_best_bid_ask_deets(market, name, size, deviation_threshold=0.05):
    best_bid, best_bid_size, second_best_bid, second_best_bid_size, top_bid = find_best_price_with_size(global_state.all_data[market]['bids'], size, reverse=True)
    best_ask, best_ask_size, second_best_ask, second_best_ask_size, top_ask = find_best_price_with_size(global_state.all_data[market]['asks'], size, reverse=False)

    if best_bid is not None and best_ask is not None:
        mid_price = (best_bid + best_ask) / 2
        bid_sum_within_n_percent = sum(size for price, size in global_state.all_data[market]['bids'].items() if best_bid <= price <= mid_price * (1 + deviation_threshold))
        ask_sum_within_n_percent = sum(size for price, size in global_state.all_data[market]['asks'].items() if mid_price * (1 - deviation_threshold) <= price <= best_ask)
    else:
        mid_price = None
        bid_sum_within_n_percent = 0
        ask_sum_within_n_percent = 0

    if name == 'token2':
        if all(x is not None for x in [best_bid, best_ask, second_best_bid, second_best_ask, top_bid, top_ask]):
            best_bid, second_best_bid, top_bid, best_ask, second_best_ask, top_ask = 1 - best_ask, 1 - second_best_ask, 1 - top_ask, 1 - best_bid, 1 - second_best_bid, 1 - top_bid
            best_bid_size, second_best_bid_size, best_ask_size, second_best_ask_size = best_ask_size, second_best_ask_size, best_bid_size, second_best_bid_size
            bid_sum_within_n_percent, ask_sum_within_n_percent = ask_sum_within_n_percent, bid_sum_within_n_percent
        else:
            if best_bid is not None and best_ask is not None:
                best_bid, best_ask = 1 - best_ask, 1 - best_bid
                best_bid_size, best_ask_size = best_ask_size, best_bid_size
            if second_best_bid is not None:
                second_best_bid = 1 - second_best_bid
            if second_best_ask is not None:
                second_best_ask = 1 - second_best_ask
            if top_bid is not None:
                top_bid = 1 - top_bid
            if top_ask is not None:
                top_ask = 1 - top_ask
            bid_sum_within_n_percent, ask_sum_within_n_percent = ask_sum_within_n_percent, bid_sum_within_n_percent

    return {
        'best_bid': best_bid, 'best_bid_size': best_bid_size,
        'second_best_bid': second_best_bid, 'second_best_bid_size': second_best_bid_size,
        'top_bid': top_bid,
        'best_ask': best_ask, 'best_ask_size': best_ask_size,
        'second_best_ask': second_best_ask, 'second_best_ask_size': second_best_ask_size,
        'top_ask': top_ask,
        'bid_sum_within_n_percent': bid_sum_within_n_percent,
        'ask_sum_within_n_percent': ask_sum_within_n_percent
    }


def find_best_price_with_size(price_dict, min_size, reverse=False):
    lst = list(price_dict.items())
    if reverse:
        lst.reverse()

    best_price, best_size = None, None
    second_best_price, second_best_size = None, None
    top_price = None
    set_best = False

    for price, size in lst:
        if top_price is None:
            top_price = price
        if set_best:
            second_best_price, second_best_size = price, size
            break
        if size > min_size:
            if best_price is None:
                best_price, best_size = price, size
                set_best = True

    return best_price, best_size, second_best_price, second_best_size, top_price

def get_order_prices(best_bid, best_bid_size, top_bid, best_ask, best_ask_size, top_ask, avgPrice, row):
    bid_price = best_bid + row['tick_size']
    ask_price = best_ask - row['tick_size']

    if best_bid_size < row['min_size'] * 1.5:
        bid_price = best_bid
    if best_ask_size < 250 * 1.5:
        ask_price = best_ask

    if bid_price >= top_ask:
        bid_price = top_bid
    if ask_price <= top_bid:
        ask_price = top_ask
    if bid_price == ask_price:
        bid_price = top_bid
        ask_price = top_ask

    if ask_price <= avgPrice and avgPrice > 0:
        ask_price = avgPrice

    return bid_price, ask_price

def round_down(number, decimals):
    factor = 10 ** decimals
    return math.floor(number * factor) / factor

def round_up(number, decimals):
    factor = 10 ** decimals
    return math.ceil(number * factor) / factor

def get_buy_sell_amount(position, bid_price, row, other_token_position=0):
    buy_amount = 0
    sell_amount = 0

    max_size = row.get('max_size', row['trade_size'])
    trade_size = row['trade_size']
    total_exposure = position + other_token_position

    if position < max_size:
        remaining_to_max = max_size - position
        buy_amount = min(trade_size, remaining_to_max)
        if position >= trade_size:
            sell_amount = min(position, trade_size)
        else:
            sell_amount = 0
    else:
        sell_amount = min(position, trade_size)
        if total_exposure < max_size * 2:
            buy_amount = trade_size
        else:
            buy_amount = 0

    if buy_amount > 0.7 * row['min_size'] and buy_amount < row['min_size']:
        buy_amount = row['min_size']

    if bid_price < 0.1 and buy_amount > 0:
        multiplier = row.get('multiplier', '')
        if multiplier != '':
            print(f"Multiplying buy amount by {int(multiplier)}")
            buy_amount = buy_amount * int(multiplier)

    return buy_amount, sell_amount
```

### File: poly_data/data_processing.py
```python
import json
from sortedcontainers import SortedDict
import poly_data.global_state as global_state
import poly_data.CONSTANTS as CONSTANTS

from trading import perform_trade
import time
import asyncio
from poly_data.data_utils import set_position, set_order, update_positions

def process_book_data(asset, json_data):
    global_state.all_data[asset] = {
        'asset_id': json_data['asset_id'],
        'bids': SortedDict(),
        'asks': SortedDict()
    }
    global_state.all_data[asset]['bids'].update({float(entry['price']): float(entry['size']) for entry in json_data['bids']})
    global_state.all_data[asset]['asks'].update({float(entry['price']): float(entry['size']) for entry in json_data['asks']})

def process_price_change(asset, side, price_level, new_size, asset_id=None):
    if asset_id and asset in global_state.all_data and asset_id != global_state.all_data[asset]['asset_id']:
        return

    if side == 'bids':
        book = global_state.all_data[asset]['bids']
    else:
        book = global_state.all_data[asset]['asks']

    if new_size == 0:
        if price_level in book:
            del book[price_level]
    else:
        book[price_level] = new_size

def process_data(json_datas, trade=True):
    if isinstance(json_datas, dict):
        json_datas = [json_datas]

    for json_data in json_datas:
        event_type = json_data['event_type']
        asset = json_data['market']

        if event_type == 'book':
            process_book_data(asset, json_data)
            if trade:
                asyncio.create_task(perform_trade(asset))

        elif event_type == 'price_change':
            for data in json_data['price_changes']:
                side = 'bids' if data['side'] == 'BUY' else 'asks'
                price_level = float(data['price'])
                new_size = float(data['size'])
                asset_id = data.get('asset_id', None)
                process_price_change(asset, side, price_level, new_size, asset_id)
                if trade:
                    asyncio.create_task(perform_trade(asset))

def add_to_performing(col, id):
    if col not in global_state.performing:
        global_state.performing[col] = set()
    if col not in global_state.performing_timestamps:
        global_state.performing_timestamps[col] = {}
    global_state.performing[col].add(id)
    global_state.performing_timestamps[col][id] = time.time()

def remove_from_performing(col, id):
    if col in global_state.performing:
        global_state.performing[col].discard(id)
    if col in global_state.performing_timestamps:
        global_state.performing_timestamps[col].pop(id, None)

def process_user_data(rows):
    for row in rows:
        market = row['market']
        side = row['side'].lower()
        token = row['asset_id']

        if token in global_state.REVERSE_TOKENS:
            col = token + "_" + side

            if row['event_type'] == 'trade':
                size = 0
                price = 0
                maker_outcome = ""
                taker_outcome = row['outcome']
                is_user_maker = False

                for maker_order in row['maker_orders']:
                    if maker_order['maker_address'].lower() == global_state.client.browser_wallet.lower():
                        print("User is maker")
                        size = float(maker_order['matched_amount'])
                        price = float(maker_order['price'])
                        is_user_maker = True
                        maker_outcome = maker_order['outcome']

                        if maker_outcome == taker_outcome:
                            side = 'buy' if side == 'sell' else 'sell'
                        else:
                            token = global_state.REVERSE_TOKENS[token]

                if not is_user_maker:
                    size = float(row['size'])
                    price = float(row['price'])
                    print("User is taker")

                print("TRADE EVENT FOR: ", row['market'], "ID: ", row['id'], "STATUS: ", row['status'], " SIDE: ", row['side'], "  MAKER OUTCOME: ", maker_outcome, " TAKER OUTCOME: ", taker_outcome, " PROCESSED SIDE: ", side, " SIZE: ", size)

                if row['status'] == 'CONFIRMED' or row['status'] == 'FAILED':
                    if row['status'] == 'FAILED':
                        print(f"Trade failed for {token}, decreasing")
                        asyncio.create_task(asyncio.sleep(2))
                        update_positions()
                    else:
                        remove_from_performing(col, row['id'])
                        print("Confirmed. Performing is ", len(global_state.performing[col]))
                        asyncio.create_task(perform_trade(market))

                elif row['status'] == 'MATCHED':
                    add_to_performing(col, row['id'])
                    print("Matched. Performing is ", len(global_state.performing[col]))
                    set_position(token, side, size, price)
                    print("Position after matching is ", global_state.positions[str(token)])
                    asyncio.create_task(perform_trade(market))

                elif row['status'] == 'MINED':
                    remove_from_performing(col, row['id'])

            elif row['event_type'] == 'order':
                print("ORDER EVENT FOR: ", row['market'], " STATUS: ", row['status'], " TYPE: ", row['type'], " SIDE: ", side, "  ORIGINAL SIZE: ", row['original_size'], " SIZE MATCHED: ", row['size_matched'])
                set_order(token, side, float(row['original_size']) - float(row['size_matched']), row['price'])
                asyncio.create_task(perform_trade(market))

    else:
        print(f"User date received for {market} but its not in")
```

### File: poly_data/data_utils.py
```python
import poly_data.global_state as global_state
from poly_data.utils import get_sheet_df
import time
import poly_data.global_state as global_state

def update_positions(avgOnly=False):
    pos_df = global_state.client.get_all_positions()
    for idx, row in pos_df.iterrows():
        asset = str(row['asset'])
        if asset in global_state.positions:
            position = global_state.positions[asset].copy()
        else:
            position = {'size': 0, 'avgPrice': 0}

        position['avgPrice'] = row['avgPrice']

        if not avgOnly:
            position['size'] = row['size']
        else:
            for col in [f"{asset}_sell", f"{asset}_buy"]:
                if col not in global_state.performing or not isinstance(global_state.performing[col], set) or len(global_state.performing[col]) == 0:
                    try:
                        old_size = position['size']
                    except:
                        old_size = 0

                    if asset in global_state.last_trade_update:
                        if time.time() - global_state.last_trade_update[asset] < 5:
                            print(f"Skipping update for {asset} because last trade update was less than 5 seconds ago")
                            continue

                    if old_size != row['size']:
                        print(f"No trades are pending. Updating position from {old_size} to {row['size']} and avgPrice to {row['avgPrice']} using API")
                    position['size'] = row['size']
                else:
                    print(f"ALERT: Skipping update for {asset} because there are trades pending for {col} looking like {global_state.performing[col]}")

        global_state.positions[asset] = position

def get_position(token):
    token = str(token)
    if token in global_state.positions:
        return global_state.positions[token]
    else:
        return {'size': 0, 'avgPrice': 0}

def set_position(token, side, size, price, source='websocket'):
    token = str(token)
    size = float(size)
    price = float(price)
    global_state.last_trade_update[token] = time.time()

    if side.lower() == 'sell':
        size *= -1

    if token in global_state.positions:
        prev_price = global_state.positions[token]['avgPrice']
        prev_size = global_state.positions[token]['size']

        if size > 0:
            if prev_size == 0:
                avgPrice_new = price
            else:
                avgPrice_new = (prev_price * prev_size + price * size) / (prev_size + size)
        elif size < 0:
            avgPrice_new = prev_price
        else:
            avgPrice_new = prev_price

        global_state.positions[token]['size'] += size
        global_state.positions[token]['avgPrice'] = avgPrice_new
    else:
        global_state.positions[token] = {'size': size, 'avgPrice': price}

    print(f"Updated position from {source}, set to ", global_state.positions[token])

def update_orders():
    all_orders = global_state.client.get_all_orders()
    orders = {}

    if len(all_orders) > 0:
        for token in all_orders['asset_id'].unique():
            if token not in orders:
                orders[str(token)] = {'buy': {'price': 0, 'size': 0}, 'sell': {'price': 0, 'size': 0}}

            curr_orders = all_orders[all_orders['asset_id'] == str(token)]
            if len(curr_orders) > 0:
                sel_orders = {}
                sel_orders['buy'] = curr_orders[curr_orders['side'] == 'BUY']
                sel_orders['sell'] = curr_orders[curr_orders['side'] == 'SELL']

                for type in ['buy', 'sell']:
                    curr = sel_orders[type]
                    if len(curr) > 1:
                        print("Multiple orders found, cancelling")
                        global_state.client.cancel_all_asset(token)
                        orders[str(token)] = {'buy': {'price': 0, 'size': 0}, 'sell': {'price': 0, 'size': 0}}
                    elif len(curr) == 1:
                        orders[str(token)][type]['price'] = float(curr.iloc[0]['price'])
                        orders[str(token)][type]['size'] = float(curr.iloc[0]['original_size'] - curr.iloc[0]['size_matched'])

    global_state.orders = orders

def get_order(token):
    token = str(token)
    if token in global_state.orders:
        if 'buy' not in global_state.orders[token]:
            global_state.orders[token]['buy'] = {'price': 0, 'size': 0}
        if 'sell' not in global_state.orders[token]:
            global_state.orders[token]['sell'] = {'price': 0, 'size': 0}
        return global_state.orders[token]
    else:
        return {'buy': {'price': 0, 'size': 0}, 'sell': {'price': 0, 'size': 0}}

def set_order(token, side, size, price):
    curr = {}
    curr = {side: {'price': 0, 'size': 0}}
    curr[side]['size'] = float(size)
    curr[side]['price'] = float(price)
    global_state.orders[str(token)] = curr
    print("Updated order, set to ", curr)

def update_markets():
    received_df, received_params = get_sheet_df()
    if len(received_df) > 0:
        if 'multiplier' not in received_df.columns:
            received_df['multiplier'] = ''
        else:
            received_df['multiplier'] = received_df['multiplier'].fillna('')
        global_state.df, global_state.params = received_df.copy(), received_params

    for _, row in global_state.df.iterrows():
        for col in ['token1', 'token2']:
            row[col] = str(row[col])

        if row['token1'] not in global_state.all_tokens:
            global_state.all_tokens.append(row['token1'])
        if row['token1'] not in global_state.REVERSE_TOKENS:
            global_state.REVERSE_TOKENS[row['token1']] = row['token2']
        if row['token2'] not in global_state.REVERSE_TOKENS:
            global_state.REVERSE_TOKENS[row['token2']] = row['token1']

        for col2 in [f"{row['token1']}_buy", f"{row['token1']}_sell", f"{row['token2']}_buy", f"{row['token2']}_sell"]:
            if col2 not in global_state.performing:
                global_state.performing[col2] = set()
```

### File: poly_data/global_state.py
```python
import threading
import pandas as pd

# Market Data
all_tokens = []
REVERSE_TOKENS = {}
all_data = {}
df = None

# Client & Parameters
client = None
params = {}
lock = threading.Lock()

# Trading State
performing = {}
performing_timestamps = {}
last_trade_update = {}
orders = {}
positions = {}
```

### File: poly_data/CONSTANTS.py
```python
MIN_MERGE_SIZE = 20
```

### File: poly_data/utils.py
```python
import json
from poly_utils.google_utils import get_spreadsheet
import pandas as pd
import os

def pretty_print(txt, dic):
    print("\n", txt, json.dumps(dic, indent=4))

def get_sheet_df(read_only=None):
    all = 'All Markets'
    sel = 'Selected Markets'

    if read_only is None:
        creds_file = 'credentials.json' if os.path.exists('credentials.json') else '../credentials.json'
        read_only = not os.path.exists(creds_file)
        if read_only:
            print("No credentials found, using read-only mode")

    try:
        spreadsheet = get_spreadsheet(read_only=read_only)
    except FileNotFoundError:
        print("No credentials found, falling back to read-only mode")
        spreadsheet = get_spreadsheet(read_only=True)

    wk = spreadsheet.worksheet(sel)
    df = pd.DataFrame(wk.get_all_records())
    df = df[df['question'] != ""].reset_index(drop=True)

    wk2 = spreadsheet.worksheet(all)
    df2 = pd.DataFrame(wk2.get_all_records())
    df2 = df2[df2['question'] != ""].reset_index(drop=True)

    result = df.merge(df2, on='question', how='inner')

    wk_p = spreadsheet.worksheet('Hyperparameters')
    records = wk_p.get_all_records()
    hyperparams, current_type = {}, None

    for r in records:
        type_value = r['type']
        if type_value and str(type_value).strip() and str(type_value) != 'nan':
            current_type = str(type_value).strip()

        if current_type:
            value = r['value']
            try:
                if isinstance(value, str) and value.replace('.', '').replace('-', '').isdigit():
                    value = float(value)
                elif isinstance(value, (int, float)):
                    value = float(value)
            except (ValueError, TypeError):
                pass
            hyperparams.setdefault(current_type, {})[r['param']] = value

    return result, hyperparams
```

### File: poly_utils/google_utils.py
```python
from google.oauth2.service_account import Credentials
import gspread
import os
import pandas as pd
import requests
import re
from dotenv import load_dotenv

load_dotenv()

def get_spreadsheet(read_only=False):
    spreadsheet_url = os.getenv("SPREADSHEET_URL")
    if not spreadsheet_url:
        raise ValueError("SPREADSHEET_URL environment variable is not set")

    creds_file = 'credentials.json' if os.path.exists('credentials.json') else '../credentials.json'

    if not os.path.exists(creds_file):
        if read_only:
            return ReadOnlySpreadsheet(spreadsheet_url)
        else:
            raise FileNotFoundError(f"Credentials file not found at {creds_file}. Use read_only=True for read-only access.")

    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials = Credentials.from_service_account_file(creds_file, scopes=scope)
    client = gspread.authorize(credentials)
    spreadsheet = client.open_by_url(spreadsheet_url)
    return spreadsheet

class ReadOnlySpreadsheet:
    def __init__(self, spreadsheet_url):
        self.spreadsheet_url = spreadsheet_url
        self.sheet_id = self._extract_sheet_id(spreadsheet_url)

    def _extract_sheet_id(self, url):
        match = re.search(r'/spreadsheets/d/([a-zA-Z0-9-_]+)', url)
        if not match:
            raise ValueError("Invalid Google Sheets URL")
        return match.group(1)

    def worksheet(self, title):
        return ReadOnlyWorksheet(self.sheet_id, title)

class ReadOnlyWorksheet:
    def __init__(self, sheet_id, title):
        self.sheet_id = sheet_id
        self.title = title

    def get_all_records(self):
        try:
            import urllib.parse
            encoded_title = urllib.parse.quote(self.title)
            sheet_gid_mapping = {
                'Full Markets': 0, 'All Markets': 1,
                'Volatility Markets': 2, 'Selected Markets': 3,
                'Hyperparameters': 4
            }
            urls_to_try = [
                f"https://docs.google.com/spreadsheets/d/{self.sheet_id}/gviz/tq?tqx=out:csv&sheet={encoded_title}",
                f"https://docs.google.com/spreadsheets/d/{self.sheet_id}/gviz/tq?tqx=out:csv&sheet={self.title}",
            ]
            if self.title in sheet_gid_mapping:
                gid = sheet_gid_mapping[self.title]
                urls_to_try.append(f"https://docs.google.com/spreadsheets/d/{self.sheet_id}/export?format=csv&gid={gid}")
            for gid in [0, 1, 2, 3, 4]:
                urls_to_try.append(f"https://docs.google.com/spreadsheets/d/{self.sheet_id}/export?format=csv&gid={gid}")

            for csv_url in urls_to_try:
                try:
                    response = requests.get(csv_url, timeout=30)
                    response.raise_for_status()
                    from io import StringIO
                    df = pd.read_csv(StringIO(response.text))
                    if not df.empty and len(df.columns) > 1:
                        if self.title == 'Hyperparameters':
                            expected_cols = ['type', 'param', 'value']
                            if all(col in df.columns for col in expected_cols):
                                return df.to_dict('records')
                            else:
                                continue
                        else:
                            return df.to_dict('records')
                except Exception as url_error:
                    continue
            return []
        except Exception as e:
            print(f"Warning: Could not fetch data from sheet '{self.title}': {e}")
            return []

    def get_all_values(self):
        try:
            csv_url = f"https://docs.google.com/spreadsheets/d/{self.sheet_id}/gviz/tq?tqx=out:csv&sheet={self.title}"
            response = requests.get(csv_url, timeout=30)
            response.raise_for_status()
            from io import StringIO
            df = pd.read_csv(StringIO(response.text))
            headers = [df.columns.tolist()]
            data = df.values.tolist()
            return headers + data
        except Exception as e:
            print(f"Warning: Could not fetch data from sheet '{self.title}': {e}")
            return []
```

### File: data_updater/find_markets.py
```python
import pandas as pd
import numpy as np
import os
import requests
import time
import warnings
import concurrent.futures
warnings.filterwarnings("ignore")

if not os.path.exists('data'):
    os.makedirs('data')

def get_sel_df(spreadsheet, sheet_name='Selected Markets'):
    try:
        wk2 = spreadsheet.worksheet(sheet_name)
        sel_df = pd.DataFrame(wk2.get_all_records())
        sel_df = sel_df[sel_df['question'] != ""].reset_index(drop=True)
        return sel_df
    except:
        return pd.DataFrame()

def get_all_markets(client):
    cursor = ""
    all_markets = []
    while True:
        try:
            markets = client.get_sampling_markets(next_cursor=cursor)
            markets_df = pd.DataFrame(markets['data'])
            cursor = markets['next_cursor']
            all_markets.append(markets_df)
            if cursor is None:
                break
        except:
            break
    all_df = pd.concat(all_markets)
    all_df = all_df.reset_index(drop=True)
    return all_df

def get_bid_ask_range(ret, TICK_SIZE):
    bid_from = ret['midpoint'] - ret['max_spread'] / 100
    bid_to = ret['best_ask']
    if bid_to == 0:
        bid_to = ret['midpoint']
    if bid_to - TICK_SIZE > ret['midpoint']:
        bid_to = ret['best_bid'] + (TICK_SIZE + 0.1 * TICK_SIZE)
    if bid_from > bid_to:
        bid_from = bid_to - (TICK_SIZE + 0.1 * TICK_SIZE)

    ask_to = ret['midpoint'] + ret['max_spread'] / 100
    ask_from = ret['best_bid']
    if ask_from == 0:
        ask_from = ret['midpoint']
    if ask_from + TICK_SIZE < ret['midpoint']:
        ask_from = ret['best_ask'] - (TICK_SIZE + 0.1 * TICK_SIZE)
    if ask_from > ask_to:
        ask_to = ask_from + (TICK_SIZE + 0.1 * TICK_SIZE)

    bid_from = max(round(bid_from, 3), 0)
    bid_to = round(bid_to, 3)
    ask_from = max(round(ask_from, 3), 0)
    ask_to = round(ask_to, 3)
    return bid_from, bid_to, ask_from, ask_to

def generate_numbers(start, end, TICK_SIZE):
    rounded_start = (int(start * 100) + 1) / 100 if start * 100 % 1 != 0 else start + TICK_SIZE
    numbers = []
    current = rounded_start
    while current < end:
        numbers.append(current)
        current += TICK_SIZE
        current = round(current, len(str(TICK_SIZE).split('.')[1]))
    return numbers

def add_formula_params(curr_df, midpoint, v, daily_reward):
    curr_df['s'] = (curr_df['price'] - midpoint).abs()
    curr_df['S'] = ((v - curr_df['s']) / v) ** 2
    curr_df['100'] = 1/curr_df['price'] * 100
    curr_df['size'] = curr_df['size'] + curr_df['100']
    curr_df['Q'] = curr_df['S'] * curr_df['size']
    curr_df['reward_per_100'] = (curr_df['Q'] / curr_df['Q'].sum()) * daily_reward / 2 / curr_df['size'] * curr_df['100']
    return curr_df

def process_single_row(row, client):
    ret = {}
    ret['question'] = row['question']
    ret['neg_risk'] = row['neg_risk']
    ret['answer1'] = row['tokens'][0]['outcome']
    ret['answer2'] = row['tokens'][1]['outcome']
    ret['min_size'] = row['rewards']['min_size']
    ret['max_spread'] = row['rewards']['max_spread']

    token1 = row['tokens'][0]['token_id']
    token2 = row['tokens'][1]['token_id']

    rate = 0
    for rate_info in row['rewards']['rates']:
        if rate_info['asset_address'].lower() == '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174'.lower():
            rate = rate_info['rewards_daily_rate']
            break

    ret['rewards_daily_rate'] = rate
    book = client.get_order_book(token1)

    bids = pd.DataFrame()
    asks = pd.DataFrame()
    try:
        bids = pd.DataFrame(book.bids).astype(float)
    except:
        pass
    try:
        asks = pd.DataFrame(book.asks).astype(float)
    except:
        pass

    try:
        ret['best_bid'] = bids.iloc[-1]['price']
    except:
        ret['best_bid'] = 0
    try:
        ret['best_ask'] = asks.iloc[-1]['price']
    except:
        ret['best_ask'] = 0

    ret['midpoint'] = (ret['best_bid'] + ret['best_ask']) / 2

    TICK_SIZE = row['minimum_tick_size']
    ret['tick_size'] = TICK_SIZE

    bid_from, bid_to, ask_from, ask_to = get_bid_ask_range(ret, TICK_SIZE)
    v = round((ret['max_spread'] / 100), 2)

    bids_df = pd.DataFrame()
    bids_df['price'] = generate_numbers(bid_from, bid_to, TICK_SIZE)
    asks_df = pd.DataFrame()
    asks_df['price'] = generate_numbers(ask_from, ask_to, TICK_SIZE)

    try:
        bids_df = bids_df.merge(bids, on='price', how='left').fillna(0)
    except:
        bids_df = pd.DataFrame()
    try:
        asks_df = asks_df.merge(asks, on='price', how='left').fillna(0)
    except:
        asks_df = pd.DataFrame()

    best_bid_reward = 0
    try:
        ret_bid = add_formula_params(bids_df, ret['midpoint'], v, rate)
        best_bid_reward = round(ret_bid['reward_per_100'].max(), 2)
    except:
        pass

    best_ask_reward = 0
    try:
        ret_ask = add_formula_params(asks_df, ret['midpoint'], v, rate)
        best_ask_reward = round(ret_ask['reward_per_100'].max(), 2)
    except:
        pass

    ret['bid_reward_per_100'] = best_bid_reward
    ret['ask_reward_per_100'] = best_ask_reward
    ret['sm_reward_per_100'] = round((best_bid_reward + best_ask_reward) / 2, 2)
    ret['gm_reward_per_100'] = round((best_bid_reward * best_ask_reward) ** 0.5, 2)

    ret['end_date_iso'] = row['end_date_iso']
    ret['market_slug'] = row['market_slug']
    ret['token1'] = token1
    ret['token2'] = token2
    ret['condition_id'] = row['condition_id']

    return ret

def get_all_results(all_df, client, max_workers=5):
    all_results = []
    def process_with_progress(args):
        idx, row = args
        try:
            return process_single_row(row, client)
        except:
            print("error fetching market")
            return None

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_with_progress, (idx, row)) for idx, row in all_df.iterrows()]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result is not None:
                all_results.append(result)
            if len(all_results) % (max_workers * 2) == 0:
                print(f'{len(all_results)} of {len(all_df)}')
    return all_results

def calculate_annualized_volatility(df, hours):
    end_time = df['t'].max()
    start_time = end_time - pd.Timedelta(hours=hours)
    window_df = df[df['t'] >= start_time]
    volatility = window_df['log_return'].std()
    annualized_volatility = volatility * np.sqrt(60 * 24 * 252)
    return round(annualized_volatility, 2)

def add_volatility(row):
    res = requests.get(f'https://clob.polymarket.com/prices-history?interval=1m&market={row["token1"]}&fidelity=10')
    price_df = pd.DataFrame(res.json()['history'])
    price_df['t'] = pd.to_datetime(price_df['t'], unit='s')
    price_df['p'] = price_df['p'].round(2)
    price_df.to_csv(f'data/{row["token1"]}.csv', index=False)
    price_df['log_return'] = np.log(price_df['p'] / price_df['p'].shift(1))

    row_dict = row.copy()
    stats = {
        '1_hour': calculate_annualized_volatility(price_df, 1),
        '3_hour': calculate_annualized_volatility(price_df, 3),
        '6_hour': calculate_annualized_volatility(price_df, 6),
        '12_hour': calculate_annualized_volatility(price_df, 12),
        '24_hour': calculate_annualized_volatility(price_df, 24),
        '7_day': calculate_annualized_volatility(price_df, 24 * 7),
        '14_day': calculate_annualized_volatility(price_df, 24 * 14),
        '30_day': calculate_annualized_volatility(price_df, 24 * 30),
        'volatility_price': price_df['p'].iloc[-1]
    }
    return {**row_dict, **stats}

def add_volatility_to_df(df, max_workers=2):
    results = []
    df = df.reset_index(drop=True)
    def process_volatility_with_progress(args):
        idx, row = args
        try:
            return add_volatility(row.to_dict())
        except:
            print("Error fetching volatility")
            return None
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_volatility_with_progress, (idx, row)) for idx, row in df.iterrows()]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result is not None:
                results.append(result)
    return pd.DataFrame(results)

def get_combined_markets(new_df, new_markets, sel_df):
    if len(sel_df) > 0:
        old_markets = new_df[new_df['question'].isin(sel_df['question'])]
        all_markets = pd.concat([old_markets, new_markets])
    else:
        all_markets = new_markets
    all_markets = all_markets.drop_duplicates('question')
    all_markets = all_markets.sort_values('gm_reward_per_100', ascending=False)
    return all_markets

def get_markets(all_results, sel_df, maker_reward=1):
    new_df = pd.DataFrame(all_results)
    new_df['spread'] = abs(new_df['best_ask'] - new_df['best_bid'])
    new_df = new_df.sort_values('rewards_daily_rate', ascending=False)
    new_df[' '] = ''
    new_df = new_df[['question', 'answer1', 'answer2', 'neg_risk', 'spread', 'best_bid', 'best_ask', 'rewards_daily_rate', 'bid_reward_per_100', 'ask_reward_per_100', 'gm_reward_per_100', 'sm_reward_per_100', 'min_size', 'max_spread', 'tick_size', 'market_slug', 'token1', 'token2', 'condition_id']]
    new_df = new_df.replace([np.inf, -np.inf], 0)
    all_data = new_df.copy()
    s_df = new_df.copy()

    making_markets = s_df[~new_df['question'].isin(sel_df['question'])]
    making_markets = making_markets.sort_values('gm_reward_per_100', ascending=False)
    making_markets = making_markets[making_markets['gm_reward_per_100'] >= maker_reward]
    all_markets = get_combined_markets(new_df, making_markets, sel_df)
    return all_data, all_markets
```

### File: data_updater/trading_utils.py
```python
from py_clob_client.constants import POLYGON
from py_clob_client.client import ClobClient
from py_clob_client.clob_types import OrderArgs, BalanceAllowanceParams, AssetType
from py_clob_client.order_builder.constants import BUY
from web3 import Web3
from web3.middleware import ExtraDataToPOAMiddleware
import json
from dotenv import load_dotenv
load_dotenv()
import time
import os

MAX_INT = 2**256 - 1

def get_clob_client():
    host = "https://clob.polymarket.com"
    key = os.getenv("PK")
    chain_id = POLYGON
    if key is None:
        print("Environment variable 'PK' cannot be found")
        return None
    try:
        client = ClobClient(host, key=key, chain_id=chain_id)
        api_creds = client.create_or_derive_api_creds()
        client.set_api_creds(api_creds)
        return client
    except Exception as ex:
        print("Error creating clob client")
        print(ex)
        return None

def approveContracts():
    web3 = Web3(Web3.HTTPProvider("https://polygon-rpc.com"))
    web3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)
    wallet = web3.eth.account.from_key(os.getenv("PK"))

    with open('erc20ABI.json', 'r') as file:
        erc20_abi = json.load(file)

    ctf_address = "0x4D97DCd97eC945f40cF65F87097ACe5EA0476045"
    erc1155_set_approval = """[{"inputs": [{ "internalType": "address", "name": "operator", "type": "address" },{ "internalType": "bool", "name": "approved", "type": "bool" }],"name": "setApprovalForAll","outputs": [],"stateMutability": "nonpayable","type": "function"}]"""

    usdc_contract = web3.eth.contract(address="0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174", abi=erc20_abi)
    ctf_contract = web3.eth.contract(address=ctf_address, abi=erc1155_set_approval)

    for address in ['0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E', '0xC5d563A36AE78145C45a50134d48A1215220f80a', '0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296']:
        usdc_nonce = web3.eth.get_transaction_count(wallet.address)
        raw_usdc_txn = usdc_contract.functions.approve(address, int(MAX_INT, 0)).build_transaction({
            "chainId": 137, "from": wallet.address, "nonce": usdc_nonce
        })
        signed_usdc_txn = web3.eth.account.sign_transaction(raw_usdc_txn, private_key=os.getenv("PK"))
        usdc_tx_receipt = web3.eth.wait_for_transaction_receipt(signed_usdc_txn, 600)
        print(f'USDC Transaction for {address} returned {usdc_tx_receipt}')
        time.sleep(1)

        ctf_nonce = web3.eth.get_transaction_count(wallet.address)
        raw_ctf_approval_txn = ctf_contract.functions.setApprovalForAll(address, True).build_transaction({
            "chainId": 137, "from": wallet.address, "nonce": ctf_nonce
        })
        signed_ctf_approval_tx = web3.eth.account.sign_transaction(raw_ctf_approval_txn, private_key=os.getenv("PK"))
        send_ctf_approval_tx = web3.eth.send_raw_transaction(signed_ctf_approval_tx.raw_transaction)
        ctf_approval_tx_receipt = web3.eth.wait_for_transaction_receipt(send_ctf_approval_tx, 600)
        print(f'CTF Transaction for {address} returned {ctf_approval_tx_receipt}')
        time.sleep(1)

def market_action(marketId, action, price, size):
    order_args = OrderArgs(price=price, size=size, side=action, token_id=marketId)
    signed_order = get_clob_client().create_order(order_args)
    try:
        resp = get_clob_client().post_order(signed_order)
        print(resp)
    except Exception as ex:
        print(ex)

def get_position(marketId):
    client = get_clob_client()
    position_res = client.get_balance_allowance(
        BalanceAllowanceParams(asset_type=AssetType.CONDITIONAL, token_id=marketId)
    )
    orderBook = client.get_order_book(marketId)
    price = float(orderBook.bids[-1].price)
    shares = int(position_res['balance']) / 1e6
    return shares * price
```

### File: data_updater/google_utils.py
```python
from google.oauth2.service_account import Credentials
import gspread
import os
import pandas as pd
import requests
import re

def get_spreadsheet(read_only=False):
    spreadsheet_url = os.getenv("SPREADSHEET_URL")
    if not spreadsheet_url:
        raise ValueError("SPREADSHEET_URL environment variable is not set")
    if not os.path.exists('credentials.json'):
        if read_only:
            return ReadOnlySpreadsheet(spreadsheet_url)
        else:
            raise FileNotFoundError("credentials.json not found.")
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials = Credentials.from_service_account_file('credentials.json', scopes=scope)
    client = gspread.authorize(credentials)
    spreadsheet = client.open_by_url(spreadsheet_url)
    return spreadsheet

class ReadOnlySpreadsheet:
    def __init__(self, spreadsheet_url):
        self.spreadsheet_url = spreadsheet_url
        self.sheet_id = self._extract_sheet_id(spreadsheet_url)
    def _extract_sheet_id(self, url):
        match = re.search(r'/spreadsheets/d/([a-zA-Z0-9-_]+)', url)
        if not match:
            raise ValueError("Invalid Google Sheets URL")
        return match.group(1)
    def worksheet(self, title):
        return ReadOnlyWorksheet(self.sheet_id, title)

class ReadOnlyWorksheet:
    def __init__(self, sheet_id, title):
        self.sheet_id = sheet_id
        self.title = title
    def get_all_records(self):
        try:
            csv_url = f"https://docs.google.com/spreadsheets/d/{self.sheet_id}/gviz/tq?tqx=out:csv&sheet={self.title}"
            response = requests.get(csv_url, timeout=30)
            response.raise_for_status()
            from io import StringIO
            df = pd.read_csv(StringIO(response.text))
            return df.to_dict('records')
        except Exception as e:
            print(f"Warning: Could not fetch data: {e}")
            return []
    def get_all_values(self):
        try:
            csv_url = f"https://docs.google.com/spreadsheets/d/{self.sheet_id}/gviz/tq?tqx=out:csv&sheet={self.title}"
            response = requests.get(csv_url, timeout=30)
            response.raise_for_status()
            from io import StringIO
            df = pd.read_csv(StringIO(response.text))
            headers = [df.columns.tolist()]
            data = df.values.tolist()
            return headers + data
        except Exception as e:
            return []
```

### File: poly_stats/account_stats.py
```python
import pandas as pd
from py_clob_client.headers.headers import create_level_2_headers
from py_clob_client.clob_types import RequestArgs
from poly_utils.google_utils import get_spreadsheet
from gspread_dataframe import set_with_dataframe
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

spreadsheet = get_spreadsheet()

def get_markets_df(wk_full):
    markets_df = pd.DataFrame(wk_full.get_all_records())
    markets_df = markets_df[['question', 'answer1', 'answer2', 'token1', 'token2']]
    markets_df['token1'] = markets_df['token1'].astype(str)
    markets_df['token2'] = markets_df['token2'].astype(str)
    return markets_df

def get_all_orders(client):
    orders = client.client.get_orders()
    orders_df = pd.DataFrame(orders)
    if len(orders_df) > 0:
        orders_df['order_size'] = orders_df['original_size'].astype('float') - orders_df['size_matched'].astype('float')
        orders_df = orders_df[['asset_id', 'order_size', 'side', 'price']]
        orders_df = orders_df.rename(columns={'side': 'order_side', 'price': 'order_price'})
        return orders_df
    else:
        return pd.DataFrame()

def get_all_positions(client):
    try:
        positions = client.get_all_positions()
        positions = positions[['asset', 'size', 'avgPrice', 'curPrice', 'percentPnl']]
        positions = positions.rename(columns={'size': 'position_size'})
        return positions
    except:
        return pd.DataFrame()

def combine_dfs(orders_df, positions, markets_df, selected_df):
    merged_df = orders_df.merge(positions, left_on=['asset_id'], right_on=['asset'], how='outer')
    merged_df['asset_id'] = merged_df['asset_id'].combine_first(merged_df['asset'])
    merged_df = merged_df.drop(columns='asset', axis=1)

    merge_token1 = merged_df.merge(markets_df, left_on='asset_id', right_on='token1', how='inner')
    merge_token1['merged_with'] = 'token1'
    merge_token2 = merged_df.merge(markets_df, left_on='asset_id', right_on='token2', how='inner')
    merge_token2['merged_with'] = 'token2'
    combined_df = pd.concat([merge_token1, merge_token2])

    combined_df['answer'] = combined_df.apply(
        lambda row: row['answer1'] if row['merged_with'] == 'token1' else row['answer2'], axis=1
    )
    combined_df = combined_df[['question', 'answer', 'order_size', 'order_side', 'order_price', 'position_size', 'avgPrice', 'curPrice']]
    combined_df['order_side'] = combined_df['order_side'].fillna('')
    combined_df = combined_df.fillna(0)
    combined_df['marketInSelected'] = combined_df['question'].isin(selected_df['question'])
    combined_df = combined_df.sort_values('question')
    combined_df = combined_df.sort_values('marketInSelected')
    return combined_df

def get_earnings(client):
    args = RequestArgs(method='GET', request_path='/rewards/user/markets')
    l2Headers = create_level_2_headers(client.signer, client.creds, args)
    url = "https://polymarket.com/api/rewards/markets"
    params = {
        "l2Headers": json.dumps(l2Headers),
        "orderBy": "earnings",
        "position": "DESC",
        "makerAddress": os.getenv('BROWSER_WALLET'),
        "authenticationType": "eoa",
        "nextCursor": '',
        "requestPath": "/rewards/user/markets"
    }
    r = requests.get(url, params=params)
    results = r.json()
    data = pd.DataFrame(results['data'])
    data['earnings'] = data['earnings'].apply(lambda x: x[0]['earnings'])
    data = data[data['earnings'] > 0].reset_index(drop=True)
    data = data[['question', 'earnings', 'earning_percentage']]
    return data

def update_stats_once(client):
    spreadsheet = get_spreadsheet()
    wk_full = spreadsheet.worksheet('Full Markets')
    wk_summary = spreadsheet.worksheet('Summary')
    wk_sel = spreadsheet.worksheet('Selected Markets')
    selected_df = pd.DataFrame(wk_sel.get_all_records())
    markets_df = get_markets_df(wk_full)

    orders_df = get_all_orders(client)
    positions = get_all_positions(client)

    if len(positions) > 0 or len(orders_df) > 0:
        combined_df = combine_dfs(orders_df, positions, markets_df, selected_df)
        earnings = get_earnings(client.client)
        combined_df = combined_df.merge(earnings, on='question', how='left')
        combined_df = combined_df.fillna(0).round(2)
        combined_df = combined_df.sort_values('earnings', ascending=False)
        combined_df = combined_df[['question', 'answer', 'order_size', 'position_size', 'marketInSelected', 'earnings', 'earning_percentage']]
        wk_summary.clear()
        set_with_dataframe(wk_summary, combined_df, include_index=False, include_column_header=True, resize=True)
    else:
        print("Position or order is empty")
```

### File: update_markets.py
```python
import time
import pandas as pd
from data_updater.trading_utils import get_clob_client
from data_updater.google_utils import get_spreadsheet
from data_updater.find_markets import get_sel_df, get_all_markets, get_all_results, get_markets, add_volatility_to_df
from gspread_dataframe import set_with_dataframe
import traceback

spreadsheet = get_spreadsheet()
client = get_clob_client()
wk_all = spreadsheet.worksheet("All Markets")
wk_vol = spreadsheet.worksheet("Volatility Markets")
sel_df = get_sel_df(spreadsheet, "Selected Markets")

def update_sheet(data, worksheet):
    all_values = worksheet.get_all_values()
    existing_num_rows = len(all_values)
    existing_num_cols = len(all_values[0]) if all_values else 0
    num_rows, num_cols = data.shape
    max_rows = max(num_rows, existing_num_rows)
    max_cols = max(num_cols, existing_num_cols)
    padded_data = pd.DataFrame('', index=range(max_rows), columns=range(max_cols))
    padded_data.iloc[:num_rows, :num_cols] = data.values
    padded_data.columns = list(data.columns) + [''] * (max_cols - num_cols)
    set_with_dataframe(worksheet, padded_data, include_index=False, include_column_header=True, resize=True)

def sort_df(df):
    mean_gm = df['gm_reward_per_100'].mean()
    std_gm = df['gm_reward_per_100'].std()
    mean_volatility = df['volatility_sum'].mean()
    std_volatility = df['volatility_sum'].std()
    df['std_gm_reward_per_100'] = (df['gm_reward_per_100'] - mean_gm) / std_gm
    df['std_volatility_sum'] = (df['volatility_sum'] - mean_volatility) / std_volatility

    def proximity_score(value):
        if 0.1 <= value <= 0.25:
            return (0.25 - value) / 0.15
        elif 0.75 <= value <= 0.9:
            return (value - 0.75) / 0.15
        else:
            return 0

    df['bid_score'] = df['best_bid'].apply(proximity_score)
    df['ask_score'] = df['best_ask'].apply(proximity_score)
    df['composite_score'] = df['std_gm_reward_per_100'] - df['std_volatility_sum'] + df['bid_score'] + df['ask_score']
    sorted_df = df.sort_values(by='composite_score', ascending=False)
    sorted_df = sorted_df.drop(columns=['std_gm_reward_per_100', 'std_volatility_sum', 'bid_score', 'ask_score', 'composite_score'])
    return sorted_df

def fetch_and_process_data():
    global spreadsheet, client, wk_all, wk_vol, sel_df
    spreadsheet = get_spreadsheet()
    client = get_clob_client()
    wk_all = spreadsheet.worksheet("All Markets")
    wk_vol = spreadsheet.worksheet("Volatility Markets")
    wk_full = spreadsheet.worksheet("Full Markets")
    sel_df = get_sel_df(spreadsheet, "Selected Markets")

    all_df = get_all_markets(client)
    all_results = get_all_results(all_df, client)
    m_data, all_markets = get_markets(all_results, sel_df, maker_reward=0.75)

    new_df = add_volatility_to_df(all_markets)
    new_df['volatility_sum'] = new_df['24_hour'] + new_df['7_day'] + new_df['14_day']
    new_df = new_df.sort_values('volatility_sum', ascending=True)
    new_df['volatilty/reward'] = ((new_df['gm_reward_per_100'] / new_df['volatility_sum']).round(2)).astype(str)

    new_df = new_df[['question', 'answer1', 'answer2', 'spread', 'rewards_daily_rate', 'gm_reward_per_100', 'sm_reward_per_100', 'bid_reward_per_100', 'ask_reward_per_100', 'volatility_sum', 'volatilty/reward', 'min_size', '1_hour', '3_hour', '6_hour', '12_hour', '24_hour', '7_day', '30_day',
                     'best_bid', 'best_ask', 'volatility_price', 'max_spread', 'tick_size',
                     'neg_risk', 'market_slug', 'token1', 'token2', 'condition_id']]

    volatility_df = new_df.copy()
    volatility_df = volatility_df[new_df['volatility_sum'] < 20]
    volatility_df = volatility_df.sort_values('gm_reward_per_100', ascending=False)
    new_df = new_df.sort_values('gm_reward_per_100', ascending=False)

    if len(new_df) > 50:
        update_sheet(new_df, wk_all)
        update_sheet(volatility_df, wk_vol)
        update_sheet(m_data, wk_full)

if __name__ == "__main__":
    while True:
        try:
            fetch_and_process_data()
            time.sleep(60 * 60)
        except Exception as e:
            traceback.print_exc()
            print(str(e))
```

### File: update_stats.py
```python
from poly_data.polymarket_client import PolymarketClient
from poly_stats.account_stats import update_stats_once
import pandas as pd
import time
import traceback

client = PolymarketClient()

if __name__ == '__main__':
    while True:
        try:
            update_stats_once(client)
        except Exception as e:
            traceback.print_exc()
        print("Now sleeping\n")
        time.sleep(60 * 60 * 3)  # 3 hours
```

### File: poly_merger/merge.js
```javascript
const { ethers } = require('ethers');
const { resolve } = require('path');
const { existsSync } = require('fs');
const { signAndExecuteSafeTransaction } = require('./safe-helpers');
const { safeAbi } = require('./safeAbi');

const localEnvPath = resolve(__dirname, '.env');
const parentEnvPath = resolve(__dirname, '../.env');
const envPath = existsSync(localEnvPath) ? localEnvPath : parentEnvPath;
require('dotenv').config({ path: envPath })

const provider = new ethers.providers.JsonRpcProvider("https://polygon-rpc.com");
const privateKey = process.env.PK;
const wallet = new ethers.Wallet(privateKey, provider);

const addresses = {
  neg_risk_adapter: '0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296',
  collateral: '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174',
  conditional_tokens: '0x4D97DCd97eC945f40cF65F87097ACe5EA0476045'
};

const negRiskAdapterAbi = [
  "function mergePositions(bytes32 conditionId, uint256 amount)"
];

const conditionalTokensAbi = [
  "function mergePositions(address collateralToken, bytes32 parentCollectionId, bytes32 conditionId, uint256[] partition, uint256 amount)"
];

async function mergePositions(amountToMerge, conditionId, isNegRiskMarket) {
    console.log(amountToMerge, conditionId, isNegRiskMarket);

    const nonce = await provider.getTransactionCount(wallet.address);
    const gasPrice = await provider.getGasPrice();
    const gasLimit = 10000000;

    let tx;
    if (isNegRiskMarket) {
      const negRiskAdapter = new ethers.Contract(addresses.neg_risk_adapter, negRiskAdapterAbi, wallet);
      tx = await negRiskAdapter.populateTransaction.mergePositions(conditionId, amountToMerge);
    } else {
      const conditionalTokens = new ethers.Contract(addresses.conditional_tokens, conditionalTokensAbi, wallet);
      tx = await conditionalTokens.populateTransaction.mergePositions(
        addresses.collateral,
        ethers.constants.HashZero,
        conditionId,
        [1, 2],
        amountToMerge
      );
    }

    const transaction = {
      ...tx,
      chainId: 137,
      gasPrice: gasPrice,
      gasLimit: gasLimit,
      nonce: nonce
    };

    const safeAddress = process.env.BROWSER_ADDRESS;
    const safe = new ethers.Contract(safeAddress, safeAbi, wallet);

    console.log("Signing Transaction")
    const txResponse = await signAndExecuteSafeTransaction(
      wallet, safe, transaction.to, transaction.data,
      { gasPrice: transaction.gasPrice, gasLimit: transaction.gasLimit }
    );

    console.log("Sent transaction. Waiting for response")
    const txReceipt = await txResponse.wait();

    console.log("merge positions " + txReceipt.transactionHash);
    return txReceipt.transactionHash;
}

const args = process.argv.slice(2);
const amountToMerge = args[0];
const conditionId = args[1];
const isNegRiskMarket = args[2] === 'true';

mergePositions(amountToMerge, conditionId, isNegRiskMarket)
  .catch(error => {
    console.error("Error merging positions:", error);
    process.exit(1);
  });
```
