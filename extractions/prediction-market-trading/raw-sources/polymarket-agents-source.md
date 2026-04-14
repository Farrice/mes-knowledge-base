# Polymarket/agents Source Material
## Fetched: 2026-04-13
## Repository: https://github.com/Polymarket/agents
## NOTE: This file contains third-party source code fetched for knowledge extraction purposes.
## The code patterns within (including uses of literal_eval etc.) are from the original repository.

### Repository Structure
```
.env.example
.github/ISSUE_TEMPLATE/bug-report---.md
.github/ISSUE_TEMPLATE/feature-request---.md
.github/workflows/dependency-review.yml
.github/workflows/docker-image.yml
.github/workflows/greetings.yml
.github/workflows/python-app.yml
.gitignore
.pre-commit-config.yaml
CONTRIBUTING.md
Dockerfile
LICENSE.md
README.md
agents/application/creator.py
agents/application/cron.py
agents/application/executor.py
agents/application/prompts.py
agents/application/trade.py
agents/connectors/chroma.py
agents/connectors/news.py
agents/connectors/search.py
agents/polymarket/gamma.py
agents/polymarket/polymarket.py
agents/utils/objects.py
agents/utils/utils.py
docs/EXAMPLE.md
docs/images/cli.png
requirements.txt
scripts/bash/build-docker.sh
scripts/bash/install.sh
scripts/bash/run-docker-dev.sh
scripts/bash/run-docker.sh
scripts/bash/start-dev.sh
scripts/python/cli.py
scripts/python/server.py
scripts/python/setup.py
tests/test.py
```

---

### File: README.md
```markdown
# Polymarket Agents

Polymarket Agents is a developer framework and set of utilities for building AI agents for Polymarket.

This code is free and publicly available under MIT License open source license.

## Features

- Integration with Polymarket API
- AI agent utilities for prediction markets
- Local and remote RAG (Retrieval-Augmented Generation) support
- Data sourcing from betting services, news providers, and web search
- Comprehensive LLM tools for prompt engineering

## Getting started

This repo is intended for use with Python 3.9

1. Clone the repository
2. Create the virtual environment: virtualenv --python=python3.9 .venv
3. Activate: source .venv/bin/activate
4. Install dependencies: pip install -r requirements.txt
5. Set up environment variables:
   POLYGON_WALLET_PRIVATE_KEY=""
   OPENAI_API_KEY=""
6. Load your wallet with USDC.
7. Try the CLI: python scripts/python/cli.py
   Or just trade: python agents/application/trade.py

## Architecture

### APIs
- Chroma.py: ChromaDB for vectorizing news/API data
- Gamma.py: GammaMarketClient for Polymarket Gamma API (market/event metadata)
- Polymarket.py: Polymarket class for API interaction and trade execution
- Objects.py: Pydantic data models

### Scripts
- cli.py: Primary user interface

## Related Repos
- py-clob-client: Python client for Polymarket CLOB
- python-order-utils: Order generation and signing utilities
- Polymarket CLOB client: TypeScript client
- Langchain: Context-aware reasoning applications
- Chroma: AI-native vector database
```

### File: .env.example
```
POLYGON_WALLET_PRIVATE_KEY=""
OPENAI_API_KEY=""
```

### File: agents/polymarket/polymarket.py
```python
import os
import pdb
import time
import requests

from dotenv import load_dotenv

from web3 import Web3
from web3.constants import MAX_INT
from web3.middleware import geth_poa_middleware

import httpx
from py_clob_client.client import ClobClient
from py_clob_client.clob_types import ApiCreds
from py_clob_client.constants import AMOY, POLYGON
from py_order_utils.builders import OrderBuilder
from py_order_utils.model import OrderData
from py_order_utils.signer import Signer
from py_clob_client.clob_types import (
    OrderArgs,
    MarketOrderArgs,
    OrderType,
    OrderBookSummary,
)
from py_clob_client.order_builder.constants import BUY

from agents.utils.objects import SimpleMarket, SimpleEvent

load_dotenv()


class Polymarket:
    def __init__(self) -> None:
        self.gamma_url = "https://gamma-api.polymarket.com"
        self.gamma_markets_endpoint = self.gamma_url + "/markets"
        self.gamma_events_endpoint = self.gamma_url + "/events"

        self.clob_url = "https://clob.polymarket.com"
        self.clob_auth_endpoint = self.clob_url + "/auth/api-key"

        self.chain_id = 137  # POLYGON
        self.private_key = os.getenv("POLYGON_WALLET_PRIVATE_KEY")
        self.polygon_rpc = "https://polygon-rpc.com"
        self.w3 = Web3(Web3.HTTPProvider(self.polygon_rpc))

        self.exchange_address = "0x4bfb41d5b3570defd03c39a9a4d8de6bd8b8982e"
        self.neg_risk_exchange_address = "0xC5d563A36AE78145C45a50134d48A1215220f80a"

        # Full USDC ERC20 ABI stored in self.erc20_approve (large JSON, omitted for brevity)
        self.erc1155_set_approval = '[{"inputs": [{ "internalType": "address", "name": "operator", "type": "address" },{ "internalType": "bool", "name": "approved", "type": "bool" }],"name": "setApprovalForAll","outputs": [],"stateMutability": "nonpayable","type": "function"}]'

        self.usdc_address = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"
        self.ctf_address = "0x4D97DCd97eC945f40cF65F87097ACe5EA0476045"

        self.web3 = Web3(Web3.HTTPProvider(self.polygon_rpc))
        self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)

        self.usdc = self.web3.eth.contract(
            address=self.usdc_address, abi=self.erc20_approve
        )
        self.ctf = self.web3.eth.contract(
            address=self.ctf_address, abi=self.erc1155_set_approval
        )

        self._init_api_keys()
        self._init_approvals(False)

    def _init_api_keys(self) -> None:
        self.client = ClobClient(
            self.clob_url, key=self.private_key, chain_id=self.chain_id
        )
        self.credentials = self.client.create_or_derive_api_creds()
        self.client.set_api_creds(self.credentials)

    def _init_approvals(self, run: bool = False) -> None:
        if not run:
            return

        priv_key = self.private_key
        pub_key = self.get_address_for_private_key()
        chain_id = self.chain_id
        web3 = self.web3
        nonce = web3.eth.get_transaction_count(pub_key)
        usdc = self.usdc
        ctf = self.ctf

        # Approves 3 contracts: CTF Exchange, Neg Risk CTF Exchange, Neg Risk Adapter
        # Each gets USDC approval (approve MAX_INT) and CTF approval (setApprovalForAll)
        # Contract addresses:
        #   CTF Exchange: 0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E
        #   Neg Risk CTF Exchange: 0xC5d563A36AE78145C45a50134d48A1215220f80a
        #   Neg Risk Adapter: 0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296
        # Each approval: build_transaction -> sign -> send -> wait_for_receipt
        pass  # Full approval code in original - 6 approval transactions total

    def get_all_markets(self) -> "list[SimpleMarket]":
        markets = []
        res = httpx.get(self.gamma_markets_endpoint)
        if res.status_code == 200:
            for market in res.json():
                try:
                    market_data = self.map_api_to_market(market)
                    markets.append(SimpleMarket(**market_data))
                except Exception as e:
                    pass
        return markets

    def filter_markets_for_trading(self, markets: "list[SimpleMarket]"):
        tradeable_markets = []
        for market in markets:
            if market.active:
                tradeable_markets.append(market)
        return tradeable_markets

    def get_market(self, token_id: str) -> SimpleMarket:
        params = {"clob_token_ids": token_id}
        res = httpx.get(self.gamma_markets_endpoint, params=params)
        if res.status_code == 200:
            data = res.json()
            market = data[0]
            return self.map_api_to_market(market, token_id)

    def map_api_to_market(self, market, token_id: str = "") -> SimpleMarket:
        market = {
            "id": int(market["id"]),
            "question": market["question"],
            "end": market["endDate"],
            "description": market["description"],
            "active": market["active"],
            "funded": market["funded"],
            "rewardsMinSize": float(market["rewardsMinSize"]),
            "rewardsMaxSpread": float(market["rewardsMaxSpread"]),
            "spread": float(market["spread"]),
            "outcomes": str(market["outcomes"]),
            "outcome_prices": str(market["outcomePrices"]),
            "clob_token_ids": str(market["clobTokenIds"]),
        }
        if token_id:
            market["clob_token_ids"] = token_id
        return market

    def get_all_events(self) -> "list[SimpleEvent]":
        events = []
        res = httpx.get(self.gamma_events_endpoint)
        if res.status_code == 200:
            for event in res.json():
                try:
                    event_data = self.map_api_to_event(event)
                    events.append(SimpleEvent(**event_data))
                except Exception as e:
                    pass
        return events

    def map_api_to_event(self, event) -> SimpleEvent:
        description = event["description"] if "description" in event.keys() else ""
        return {
            "id": int(event["id"]),
            "ticker": event["ticker"],
            "slug": event["slug"],
            "title": event["title"],
            "description": description,
            "active": event["active"],
            "closed": event["closed"],
            "archived": event["archived"],
            "new": event["new"],
            "featured": event["featured"],
            "restricted": event["restricted"],
            "end": event["endDate"],
            "markets": ",".join([x["id"] for x in event["markets"]]),
        }

    def filter_events_for_trading(self, events):
        tradeable_events = []
        for event in events:
            if event.active and not event.restricted and not event.archived and not event.closed:
                tradeable_events.append(event)
        return tradeable_events

    def get_all_tradeable_events(self):
        all_events = self.get_all_events()
        return self.filter_events_for_trading(all_events)

    def get_sampling_simplified_markets(self):
        markets = []
        raw_sampling_simplified_markets = self.client.get_sampling_simplified_markets()
        for raw_market in raw_sampling_simplified_markets["data"]:
            token_one_id = raw_market["tokens"][0]["token_id"]
            market = self.get_market(token_one_id)
            markets.append(market)
        return markets

    def get_orderbook(self, token_id: str) -> OrderBookSummary:
        return self.client.get_order_book(token_id)

    def get_orderbook_price(self, token_id: str) -> float:
        return float(self.client.get_price(token_id))

    def get_address_for_private_key(self):
        account = self.w3.eth.account.from_key(str(self.private_key))
        return account.address

    def build_order(self, market_token, amount, nonce=None, side="BUY", expiration="0"):
        signer = Signer(self.private_key)
        builder = OrderBuilder(self.exchange_address, self.chain_id, signer)
        buy = side == "BUY"
        side_int = 0 if buy else 1
        maker_amount = amount if buy else 0
        taker_amount = amount if not buy else 0
        order_data = OrderData(
            maker=self.get_address_for_private_key(),
            tokenId=market_token,
            makerAmount=maker_amount,
            takerAmount=taker_amount,
            feeRateBps="1",
            nonce=nonce or str(round(time.time())),
            side=side_int,
            expiration=expiration,
        )
        order = builder.build_signed_order(order_data)
        return order

    def execute_order(self, price, size, side, token_id) -> str:
        return self.client.create_and_post_order(
            OrderArgs(price=price, size=size, side=side, token_id=token_id)
        )

    def execute_market_order(self, market, amount) -> str:
        # Uses ast.literal_eval to parse clob_token_ids from market metadata
        import ast
        token_id = ast.literal_eval(market[0].dict()["metadata"]["clob_token_ids"])[1]
        order_args = MarketOrderArgs(token_id=token_id, amount=amount)
        signed_order = self.client.create_market_order(order_args)
        resp = self.client.post_order(signed_order, orderType=OrderType.FOK)
        return resp

    def get_usdc_balance(self) -> float:
        balance_res = self.usdc.functions.balanceOf(
            self.get_address_for_private_key()
        ).call()
        return float(balance_res / 10e5)
```

### File: agents/polymarket/gamma.py
```python
import httpx
import json

from agents.polymarket.polymarket import Polymarket
from agents.utils.objects import Market, PolymarketEvent, ClobReward, Tag


class GammaMarketClient:
    def __init__(self):
        self.gamma_url = "https://gamma-api.polymarket.com"
        self.gamma_markets_endpoint = self.gamma_url + "/markets"
        self.gamma_events_endpoint = self.gamma_url + "/events"

    def parse_pydantic_market(self, market_object: dict) -> Market:
        try:
            if "clobRewards" in market_object:
                clob_rewards = []
                for clob_rewards_obj in market_object["clobRewards"]:
                    clob_rewards.append(ClobReward(**clob_rewards_obj))
                market_object["clobRewards"] = clob_rewards

            if "events" in market_object:
                events = []
                for market_event_obj in market_object["events"]:
                    events.append(self.parse_nested_event(market_event_obj))
                market_object["events"] = events

            if "outcomePrices" in market_object:
                market_object["outcomePrices"] = json.loads(market_object["outcomePrices"])
            if "clobTokenIds" in market_object:
                market_object["clobTokenIds"] = json.loads(market_object["clobTokenIds"])

            return Market(**market_object)
        except Exception as err:
            print(f"[parse_market] Caught exception: {err}")

    def parse_nested_event(self, event_object) -> PolymarketEvent:
        try:
            if "tags" in event_object:
                tags = []
                for tag in event_object["tags"]:
                    tags.append(Tag(**tag))
                event_object["tags"] = tags
            return PolymarketEvent(**event_object)
        except Exception as err:
            print(f"[parse_event] Caught exception: {err}")

    def get_markets(self, querystring_params={}, parse_pydantic=False, local_file_path=None):
        response = httpx.get(self.gamma_markets_endpoint, params=querystring_params)
        if response.status_code == 200:
            data = response.json()
            if local_file_path is not None:
                with open(local_file_path, "w+") as out_file:
                    json.dump(data, out_file)
            elif not parse_pydantic:
                return data
            else:
                markets = []
                for market_object in data:
                    markets.append(self.parse_pydantic_market(market_object))
                return markets
        else:
            raise Exception()

    def get_events(self, querystring_params={}, parse_pydantic=False, local_file_path=None):
        response = httpx.get(self.gamma_events_endpoint, params=querystring_params)
        if response.status_code == 200:
            data = response.json()
            if local_file_path is not None:
                with open(local_file_path, "w+") as out_file:
                    json.dump(data, out_file)
            elif not parse_pydantic:
                return data
            else:
                events = []
                for market_event_obj in data:
                    events.append(self.parse_event(market_event_obj))
                return events
        else:
            raise Exception()

    def get_all_markets(self, limit=2):
        return self.get_markets(querystring_params={"limit": limit})

    def get_all_events(self, limit=2):
        return self.get_events(querystring_params={"limit": limit})

    def get_current_markets(self, limit=4):
        return self.get_markets(querystring_params={
            "active": True, "closed": False, "archived": False, "limit": limit,
        })

    def get_all_current_markets(self, limit=100):
        offset = 0
        all_markets = []
        while True:
            params = {
                "active": True, "closed": False, "archived": False,
                "limit": limit, "offset": offset,
            }
            market_batch = self.get_markets(querystring_params=params)
            all_markets.extend(market_batch)
            if len(market_batch) < limit:
                break
            offset += limit
        return all_markets

    def get_current_events(self, limit=4):
        return self.get_events(querystring_params={
            "active": True, "closed": False, "archived": False, "limit": limit,
        })

    def get_clob_tradable_markets(self, limit=2):
        return self.get_markets(querystring_params={
            "active": True, "closed": False, "archived": False,
            "limit": limit, "enableOrderBook": True,
        })

    def get_market(self, market_id: int):
        url = self.gamma_markets_endpoint + "/" + str(market_id)
        response = httpx.get(url)
        return response.json()
```

### File: agents/application/executor.py
```python
import os
import json
import re
from typing import List, Dict, Any
import math

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

from agents.polymarket.gamma import GammaMarketClient as Gamma
from agents.connectors.chroma import PolymarketRAG as Chroma
from agents.utils.objects import SimpleEvent, SimpleMarket
from agents.application.prompts import Prompter
from agents.polymarket.polymarket import Polymarket

def retain_keys(data, keys_to_retain):
    if isinstance(data, dict):
        return {key: retain_keys(value, keys_to_retain)
                for key, value in data.items() if key in keys_to_retain}
    elif isinstance(data, list):
        return [retain_keys(item, keys_to_retain) for item in data]
    else:
        return data

class Executor:
    def __init__(self, default_model='gpt-3.5-turbo-16k') -> None:
        load_dotenv()
        max_token_model = {'gpt-3.5-turbo-16k':15000, 'gpt-4-1106-preview':95000}
        self.token_limit = max_token_model.get(default_model)
        self.prompter = Prompter()
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.llm = ChatOpenAI(model=default_model, temperature=0)
        self.gamma = Gamma()
        self.chroma = Chroma()
        self.polymarket = Polymarket()

    def get_llm_response(self, user_input: str) -> str:
        system_message = SystemMessage(content=str(self.prompter.market_analyst()))
        human_message = HumanMessage(content=user_input)
        messages = [system_message, human_message]
        result = self.llm.invoke(messages)
        return result.content

    def get_superforecast(self, event_title, market_question, outcome) -> str:
        messages = self.prompter.superforecaster(
            description=event_title, question=market_question, outcome=outcome
        )
        result = self.llm.invoke(messages)
        return result.content

    def estimate_tokens(self, text: str) -> int:
        return len(text) // 4

    def process_data_chunk(self, data1, data2, user_input: str) -> str:
        system_message = SystemMessage(
            content=str(self.prompter.prompts_polymarket(data1=data1, data2=data2))
        )
        human_message = HumanMessage(content=user_input)
        messages = [system_message, human_message]
        result = self.llm.invoke(messages)
        return result.content

    def divide_list(self, original_list, i):
        sublist_size = math.ceil(len(original_list) / i)
        return [original_list[j:j+sublist_size] for j in range(0, len(original_list), sublist_size)]

    def get_polymarket_llm(self, user_input: str) -> str:
        data1 = self.gamma.get_current_events()
        data2 = self.gamma.get_current_markets()
        combined_data = str(self.prompter.prompts_polymarket(data1=data1, data2=data2))
        total_tokens = self.estimate_tokens(combined_data)
        token_limit = self.token_limit

        if total_tokens <= token_limit:
            return self.process_data_chunk(data1, data2, user_input)
        else:
            group_size = (total_tokens // token_limit) + 1
            useful_keys = ['id','questionID','description','liquidity','clobTokenIds',
                          'outcomes','outcomePrices','volume','startDate','endDate',
                          'question','questionID','events']
            data1 = retain_keys(data1, useful_keys)
            cut_1 = self.divide_list(data1, group_size)
            cut_2 = self.divide_list(data2, group_size)
            cut_data_12 = zip(cut_1, cut_2)
            results = []
            for cut_data in cut_data_12:
                result = self.process_data_chunk(cut_data[0], cut_data[1], user_input)
                results.append(result)
            return " ".join(results)

    def filter_events(self, events) -> str:
        prompt = self.prompter.filter_events(events)
        result = self.llm.invoke(prompt)
        return result.content

    def filter_events_with_rag(self, events) -> str:
        prompt = self.prompter.filter_events()
        return self.chroma.events(events, prompt)

    def map_filtered_events_to_markets(self, filtered_events):
        markets = []
        for e in filtered_events:
            data = json.loads(e[0].json())
            market_ids = data["metadata"]["markets"].split(",")
            for market_id in market_ids:
                market_data = self.gamma.get_market(market_id)
                formatted_market_data = self.polymarket.map_api_to_market(market_data)
                markets.append(formatted_market_data)
        return markets

    def filter_markets(self, markets):
        prompt = self.prompter.filter_markets()
        return self.chroma.markets(markets, prompt)

    def source_best_trade(self, market_object) -> str:
        market_document = market_object[0].dict()
        market = market_document["metadata"]
        import ast
        outcome_prices = ast.literal_eval(market["outcome_prices"])
        outcomes = ast.literal_eval(market["outcomes"])
        question = market["question"]
        description = market_document["page_content"]

        prompt = self.prompter.superforecaster(question, description, outcomes)
        result = self.llm.invoke(prompt)
        content = result.content

        prompt = self.prompter.one_best_trade(content, outcomes, outcome_prices)
        result = self.llm.invoke(prompt)
        return result.content

    def format_trade_prompt_for_execution(self, best_trade: str) -> float:
        data = best_trade.split(",")
        size = re.findall(r"\d+\.\d+", data[1])[0]
        usdc_balance = self.polymarket.get_usdc_balance()
        return float(size) * usdc_balance

    def source_best_market_to_create(self, filtered_markets) -> str:
        prompt = self.prompter.create_new_market(filtered_markets)
        result = self.llm.invoke(prompt)
        return result.content
```

### File: agents/application/trade.py
```python
from agents.application.executor import Executor as Agent
from agents.polymarket.gamma import GammaMarketClient as Gamma
from agents.polymarket.polymarket import Polymarket

import shutil


class Trader:
    def __init__(self):
        self.polymarket = Polymarket()
        self.gamma = Gamma()
        self.agent = Agent()

    def pre_trade_logic(self) -> None:
        self.clear_local_dbs()

    def clear_local_dbs(self) -> None:
        try:
            shutil.rmtree("local_db_events")
        except:
            pass
        try:
            shutil.rmtree("local_db_markets")
        except:
            pass

    def one_best_trade(self) -> None:
        """
        one_best_trade evaluates all events, markets, and orderbooks
        leverages all available information sources accessible to the agent
        then executes that trade without human intervention
        """
        try:
            self.pre_trade_logic()

            events = self.polymarket.get_all_tradeable_events()
            print(f"1. FOUND {len(events)} EVENTS")

            filtered_events = self.agent.filter_events_with_rag(events)
            print(f"2. FILTERED {len(filtered_events)} EVENTS")

            markets = self.agent.map_filtered_events_to_markets(filtered_events)
            print(f"3. FOUND {len(markets)} MARKETS")

            filtered_markets = self.agent.filter_markets(markets)
            print(f"4. FILTERED {len(filtered_markets)} MARKETS")

            market = filtered_markets[0]
            best_trade = self.agent.source_best_trade(market)
            print(f"5. CALCULATED TRADE {best_trade}")

            amount = self.agent.format_trade_prompt_for_execution(best_trade)
            # Please refer to TOS before uncommenting: polymarket.com/tos
            # trade = self.polymarket.execute_market_order(market, amount)

        except Exception as e:
            print(f"Error {e} \n \n Retrying")
            self.one_best_trade()


if __name__ == "__main__":
    t = Trader()
    t.one_best_trade()
```

### File: agents/application/creator.py
```python
from agents.application.executor import Executor as Agent
from agents.polymarket.gamma import GammaMarketClient as Gamma
from agents.polymarket.polymarket import Polymarket


class Creator:
    def __init__(self):
        self.polymarket = Polymarket()
        self.gamma = Gamma()
        self.agent = Agent()

    def one_best_market(self):
        try:
            events = self.polymarket.get_all_tradeable_events()
            print(f"1. FOUND {len(events)} EVENTS")

            filtered_events = self.agent.filter_events_with_rag(events)
            print(f"2. FILTERED {len(filtered_events)} EVENTS")

            markets = self.agent.map_filtered_events_to_markets(filtered_events)
            print(f"3. FOUND {len(markets)} MARKETS")

            filtered_markets = self.agent.filter_markets(markets)
            print(f"4. FILTERED {len(filtered_markets)} MARKETS")

            best_market = self.agent.source_best_market_to_create(filtered_markets)
            print(f"5. IDEA FOR NEW MARKET {best_market}")
            return best_market

        except Exception as e:
            print(f"Error {e} \n \n Retrying")
            self.one_best_market()


if __name__ == "__main__":
    c = Creator()
    c.one_best_market()
```

### File: agents/application/cron.py
```python
from agents.application.trade import Trader
import time
from scheduler import Scheduler
from scheduler.trigger import Monday


class Scheduler:
    def __init__(self) -> None:
        self.trader = Trader()
        self.schedule = Scheduler()

    def start(self) -> None:
        while True:
            self.schedule.exec_jobs()
            time.sleep(1)


class TradingAgent(Scheduler):
    def __init__(self) -> None:
        super()
        self.trader = Trader()
        self.weekly(Monday(), self.trader.one_best_trade)
```

### File: agents/utils/objects.py
```python
from __future__ import annotations
from typing import Optional, Union
from pydantic import BaseModel


class Trade(BaseModel):
    id: int
    taker_order_id: str
    market: str
    asset_id: str
    side: str
    size: str
    fee_rate_bps: str
    price: str
    status: str
    match_time: str
    last_update: str
    outcome: str
    maker_address: str
    owner: str
    transaction_hash: str
    bucket_index: str
    maker_orders: list[str]
    type: str


class SimpleMarket(BaseModel):
    id: int
    question: str
    end: str
    description: str
    active: bool
    funded: bool
    rewardsMinSize: float
    rewardsMaxSpread: float
    spread: float
    outcomes: str
    outcome_prices: str
    clob_token_ids: Optional[str]


class ClobReward(BaseModel):
    id: str
    conditionId: str
    assetAddress: str
    rewardsAmount: float
    rewardsDailyRate: int
    startDate: str
    endDate: str


class Tag(BaseModel):
    id: str
    label: Optional[str] = None
    slug: Optional[str] = None
    forceShow: Optional[bool] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    _sync: Optional[bool] = None


class PolymarketEvent(BaseModel):
    id: str
    ticker: Optional[str] = None
    slug: Optional[str] = None
    title: Optional[str] = None
    startDate: Optional[str] = None
    creationDate: Optional[str] = None
    endDate: Optional[str] = None
    image: Optional[str] = None
    icon: Optional[str] = None
    active: Optional[bool] = None
    closed: Optional[bool] = None
    archived: Optional[bool] = None
    new: Optional[bool] = None
    featured: Optional[bool] = None
    restricted: Optional[bool] = None
    liquidity: Optional[float] = None
    volume: Optional[float] = None
    reviewStatus: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    competitive: Optional[float] = None
    volume24hr: Optional[float] = None
    enableOrderBook: Optional[bool] = None
    liquidityClob: Optional[float] = None
    _sync: Optional[bool] = None
    commentCount: Optional[int] = None
    markets: Optional[list[Market]] = None
    tags: Optional[list[Tag]] = None
    cyom: Optional[bool] = None
    showAllOutcomes: Optional[bool] = None
    showMarketImages: Optional[bool] = None


class Market(BaseModel):
    id: int
    question: Optional[str] = None
    conditionId: Optional[str] = None
    slug: Optional[str] = None
    resolutionSource: Optional[str] = None
    endDate: Optional[str] = None
    liquidity: Optional[float] = None
    startDate: Optional[str] = None
    image: Optional[str] = None
    icon: Optional[str] = None
    description: Optional[str] = None
    outcome: Optional[list] = None
    outcomePrices: Optional[list] = None
    volume: Optional[float] = None
    active: Optional[bool] = None
    closed: Optional[bool] = None
    marketMakerAddress: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    new: Optional[bool] = None
    featured: Optional[bool] = None
    submitted_by: Optional[str] = None
    archived: Optional[bool] = None
    resolvedBy: Optional[str] = None
    restricted: Optional[bool] = None
    groupItemTitle: Optional[str] = None
    groupItemThreshold: Optional[int] = None
    questionID: Optional[str] = None
    enableOrderBook: Optional[bool] = None
    orderPriceMinTickSize: Optional[float] = None
    orderMinSize: Optional[int] = None
    volumeNum: Optional[float] = None
    liquidityNum: Optional[float] = None
    endDateIso: Optional[str] = None
    startDateIso: Optional[str] = None
    hasReviewedDates: Optional[bool] = None
    volume24hr: Optional[float] = None
    clobTokenIds: Optional[list] = None
    umaBond: Optional[int] = None
    umaReward: Optional[int] = None
    volume24hrClob: Optional[float] = None
    volumeClob: Optional[float] = None
    liquidityClob: Optional[float] = None
    acceptingOrders: Optional[bool] = None
    negRisk: Optional[bool] = None
    commentCount: Optional[int] = None
    _sync: Optional[bool] = None
    events: Optional[list[PolymarketEvent]] = None
    ready: Optional[bool] = None
    deployed: Optional[bool] = None
    funded: Optional[bool] = None
    deployedTimestamp: Optional[str] = None
    acceptingOrdersTimestamp: Optional[str] = None
    cyom: Optional[bool] = None
    competitive: Optional[float] = None
    pagerDutyNotificationEnabled: Optional[bool] = None
    reviewStatus: Optional[str] = None
    approved: Optional[bool] = None
    clobRewards: Optional[list[ClobReward]] = None
    rewardsMinSize: Optional[int] = None
    rewardsMaxSpread: Optional[float] = None
    spread: Optional[float] = None


class ComplexMarket(BaseModel):
    id: int
    condition_id: str
    question_id: str
    tokens: Union[str, str]
    rewards: str
    minimum_order_size: str
    minimum_tick_size: str
    description: str
    category: str
    end_date_iso: str
    game_start_time: str
    question: str
    market_slug: str
    min_incentive_size: str
    max_incentive_spread: str
    active: bool
    closed: bool
    seconds_delay: int
    icon: str
    fpmm: str
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class SimpleEvent(BaseModel):
    id: int
    ticker: str
    slug: str
    title: str
    description: str
    end: str
    active: bool
    closed: bool
    archived: bool
    restricted: bool
    new: bool
    featured: bool
    restricted: bool
    markets: str


class Source(BaseModel):
    id: Optional[str]
    name: Optional[str]


class Article(BaseModel):
    source: Optional[Source]
    author: Optional[str]
    title: Optional[str]
    description: Optional[str]
    url: Optional[str]
    urlToImage: Optional[str]
    publishedAt: Optional[str]
    content: Optional[str]
```

### File: agents/utils/utils.py
```python
import json


def parse_camel_case(key) -> str:
    output = ""
    for char in key:
        if char.isupper():
            output += " "
            output += char.lower()
        else:
            output += char
    return output


def preprocess_market_object(market_object: dict) -> dict:
    description = market_object["description"]
    for k, v in market_object.items():
        if k == "description":
            continue
        if isinstance(v, bool):
            description += f' This market is{" not" if not v else ""} {parse_camel_case(k)}.'
        if k in ["volume", "liquidity"]:
            description += f" This market has a current {k} of {v}."
    market_object["description"] = description
    return market_object


def preprocess_local_json(file_path, preprocessor_function) -> None:
    with open(file_path, "r+") as open_file:
        data = json.load(open_file)
    output = []
    for obj in data:
        preprocessed_json = preprocessor_function(obj)
        output.append(preprocessed_json)
    split_path = file_path.split(".")
    new_file_path = split_path[0] + "_preprocessed." + split_path[1]
    with open(new_file_path, "w+") as output_file:
        json.dump(output, output_file)


def metadata_func(record: dict, metadata: dict) -> dict:
    for k, v in record.items():
        metadata[k] = v
    del metadata["description"]
    del metadata["events"]
    return metadata
```

### File: agents/connectors/chroma.py
```python
import json
import os
import time

from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import JSONLoader
from langchain_community.vectorstores.chroma import Chroma

from agents.polymarket.gamma import GammaMarketClient
from agents.utils.objects import SimpleEvent, SimpleMarket


class PolymarketRAG:
    def __init__(self, local_db_directory=None, embedding_function=None) -> None:
        self.gamma_client = GammaMarketClient()
        self.local_db_directory = local_db_directory
        self.embedding_function = embedding_function

    def load_json_from_local(self, json_file_path=None, vector_db_directory="./local_db") -> None:
        loader = JSONLoader(
            file_path=json_file_path, jq_schema=".[].description", text_content=False
        )
        loaded_docs = loader.load()
        embedding_function = OpenAIEmbeddings(model="text-embedding-3-small")
        Chroma.from_documents(loaded_docs, embedding_function, persist_directory=vector_db_directory)

    def create_local_markets_rag(self, local_directory="./local_db") -> None:
        all_markets = self.gamma_client.get_all_current_markets()
        if not os.path.isdir(local_directory):
            os.mkdir(local_directory)
        local_file_path = f"{local_directory}/all-current-markets_{time.time()}.json"
        with open(local_file_path, "w+") as output_file:
            json.dump(all_markets, output_file)
        self.load_json_from_local(json_file_path=local_file_path, vector_db_directory=local_directory)

    def query_local_markets_rag(self, local_directory=None, query=None):
        embedding_function = OpenAIEmbeddings(model="text-embedding-3-small")
        local_db = Chroma(persist_directory=local_directory, embedding_function=embedding_function)
        response_docs = local_db.similarity_search_with_score(query=query)
        return response_docs

    def events(self, events, prompt: str):
        local_events_directory = "./local_db_events"
        if not os.path.isdir(local_events_directory):
            os.mkdir(local_events_directory)
        local_file_path = f"{local_events_directory}/events.json"
        dict_events = [x.dict() for x in events]
        with open(local_file_path, "w+") as output_file:
            json.dump(dict_events, output_file)

        def metadata_func(record, metadata):
            metadata["id"] = record.get("id")
            metadata["markets"] = record.get("markets")
            return metadata

        loader = JSONLoader(
            file_path=local_file_path, jq_schema=".[]",
            content_key="description", text_content=False, metadata_func=metadata_func,
        )
        loaded_docs = loader.load()
        embedding_function = OpenAIEmbeddings(model="text-embedding-3-small")
        vector_db_directory = f"{local_events_directory}/chroma"
        local_db = Chroma.from_documents(loaded_docs, embedding_function, persist_directory=vector_db_directory)
        return local_db.similarity_search_with_score(query=prompt)

    def markets(self, markets, prompt: str):
        local_events_directory = "./local_db_markets"
        if not os.path.isdir(local_events_directory):
            os.mkdir(local_events_directory)
        local_file_path = f"{local_events_directory}/markets.json"
        with open(local_file_path, "w+") as output_file:
            json.dump(markets, output_file)

        def metadata_func(record, metadata):
            metadata["id"] = record.get("id")
            metadata["outcomes"] = record.get("outcomes")
            metadata["outcome_prices"] = record.get("outcome_prices")
            metadata["question"] = record.get("question")
            metadata["clob_token_ids"] = record.get("clob_token_ids")
            return metadata

        loader = JSONLoader(
            file_path=local_file_path, jq_schema=".[]",
            content_key="description", text_content=False, metadata_func=metadata_func,
        )
        loaded_docs = loader.load()
        embedding_function = OpenAIEmbeddings(model="text-embedding-3-small")
        vector_db_directory = f"{local_events_directory}/chroma"
        local_db = Chroma.from_documents(loaded_docs, embedding_function, persist_directory=vector_db_directory)
        return local_db.similarity_search_with_score(query=prompt)
```

### File: agents/connectors/news.py
```python
from datetime import datetime
import os

from newsapi import NewsApiClient

from agents.utils.objects import Article


class News:
    def __init__(self) -> None:
        self.configs = {
            "language": "en",
            "country": "us",
            "top_headlines": "https://newsapi.org/v2/top-headlines?country=us&apiKey=",
            "base_url": "https://newsapi.org/v2/",
        }
        self.categories = {
            "business", "entertainment", "general",
            "health", "science", "sports", "technology",
        }
        self.API = NewsApiClient(os.getenv("NEWSAPI_API_KEY"))

    def get_articles_for_cli_keywords(self, keywords):
        query_words = keywords.split(",")
        all_articles = self.get_articles_for_options(query_words)
        article_objects = []
        for _, articles in all_articles.items():
            for article in articles:
                article_objects.append(Article(**article))
        return article_objects

    def get_top_articles_for_market(self, market_object: dict):
        return self.API.get_top_headlines(
            language="en", country="usa", q=market_object["description"]
        )

    def get_articles_for_options(self, market_options, date_start=None, date_end=None):
        all_articles = {}
        if not date_start and not date_end:
            for option in market_options:
                response_dict = self.API.get_top_headlines(
                    q=option.strip(),
                    language=self.configs["language"],
                    country=self.configs["country"],
                )
                all_articles[option] = response_dict["articles"]
        else:
            for option in market_options:
                response_dict = self.API.get_everything(
                    q=option.strip(),
                    language=self.configs["language"],
                    country=self.configs["country"],
                    from_param=date_start,
                    to=date_end,
                )
                all_articles[option] = response_dict["articles"]
        return all_articles

    def get_category(self, market_object: dict) -> str:
        news_category = "general"
        market_category = market_object["category"]
        if market_category in self.categories:
            news_category = market_category
        return news_category
```

### File: agents/connectors/search.py
```python
import os

from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

openai_api_key = os.getenv("OPEN_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

tavily_client = TavilyClient(api_key=tavily_api_key)
context = tavily_client.get_search_context(query="Will Biden drop out of the race?")
```

### File: scripts/python/cli.py
```python
import typer
from devtools import pprint

from agents.polymarket.polymarket import Polymarket
from agents.connectors.chroma import PolymarketRAG
from agents.connectors.news import News
from agents.application.trade import Trader
from agents.application.executor import Executor
from agents.application.creator import Creator

app = typer.Typer()
polymarket = Polymarket()
newsapi_client = News()
polymarket_rag = PolymarketRAG()


@app.command()
def get_all_markets(limit: int = 5, sort_by: str = "spread") -> None:
    markets = polymarket.get_all_markets()
    markets = polymarket.filter_markets_for_trading(markets)
    if sort_by == "spread":
        markets = sorted(markets, key=lambda x: x.spread, reverse=True)
    markets = markets[:limit]
    pprint(markets)


@app.command()
def get_relevant_news(keywords: str) -> None:
    articles = newsapi_client.get_articles_for_cli_keywords(keywords)
    pprint(articles)


@app.command()
def get_all_events(limit: int = 5, sort_by: str = "number_of_markets") -> None:
    events = polymarket.get_all_events()
    events = polymarket.filter_events_for_trading(events)
    if sort_by == "number_of_markets":
        events = sorted(events, key=lambda x: len(x.markets), reverse=True)
    events = events[:limit]
    pprint(events)


@app.command()
def create_local_markets_rag(local_directory: str) -> None:
    polymarket_rag.create_local_markets_rag(local_directory=local_directory)


@app.command()
def query_local_markets_rag(vector_db_directory: str, query: str) -> None:
    response = polymarket_rag.query_local_markets_rag(
        local_directory=vector_db_directory, query=query
    )
    pprint(response)


@app.command()
def ask_superforecaster(event_title: str, market_question: str, outcome: str) -> None:
    executor = Executor()
    response = executor.get_superforecast(
        event_title=event_title, market_question=market_question, outcome=outcome
    )
    print(f"Response:{response}")


@app.command()
def create_market() -> None:
    c = Creator()
    market_description = c.one_best_market()
    print(f"market_description: str = {market_description}")


@app.command()
def ask_llm(user_input: str) -> None:
    executor = Executor()
    response = executor.get_llm_response(user_input)
    print(f"LLM Response: {response}")


@app.command()
def ask_polymarket_llm(user_input: str) -> None:
    executor = Executor()
    response = executor.get_polymarket_llm(user_input=user_input)
    print(f"LLM + current markets&events response: {response}")


@app.command()
def run_autonomous_trader() -> None:
    trader = Trader()
    trader.one_best_trade()


if __name__ == "__main__":
    app()
```

### File: requirements.txt (key dependencies)
```
py_clob_client==0.17.5
py_order_utils==0.3.2
web3==6.11.0
websockets==12.0
eth-account==0.13.1
langchain==0.2.11
langchain-openai==0.1.19
langchain-chroma==0.1.2
chromadb==0.5.5
openai==1.37.1
httpx==0.27.0
pydantic==2.8.2
python-dotenv==1.0.1
requests==2.32.3
newsapi-python==0.2.7
tavily-python==0.3.5
typer==0.12.3
```
