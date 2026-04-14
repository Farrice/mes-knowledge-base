"""
Constants for the Prediction Market Arb Platform.

All API endpoints, contract addresses, ICAO station mappings, rate limits,
and platform timing parameters. Sourced from Phase 0 MES 3.0 extractions.
"""

# =============================================================================
# API ENDPOINTS
# =============================================================================

CLOB_URL = "https://clob.polymarket.com"
GAMMA_URL = "https://gamma-api.polymarket.com"
DATA_URL = "https://data-api.polymarket.com"

WS_MARKET_URL = "wss://ws-subscriptions-clob.polymarket.com/ws/market"
WS_USER_URL = "wss://ws-subscriptions-clob.polymarket.com/ws/user"
WS_SPORTS_URL = "wss://sports-api.polymarket.com/ws"
WS_RTDS_URL = "wss://ws-live-data.polymarket.com"

# =============================================================================
# POLYGON SMART CONTRACTS (Chain ID 137)
# =============================================================================

POLYGON_CHAIN_ID = 137
POLYGON_RPC = "https://polygon-rpc.com"

CTF_EXCHANGE = "0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E"
NEG_RISK_CTF_EXCHANGE = "0xC5d563A36AE78145C45a50134d48A1215220f80a"
NEG_RISK_ADAPTER = "0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296"
CONDITIONAL_TOKENS = "0x4D97DCd97eC945f40cF65F87097ACe5EA0476045"
USDC_E = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"

# USDC.e has 6 decimals on Polygon
USDC_DECIMALS = 6

# =============================================================================
# RATE LIMITS (per 10-second window unless noted)
# =============================================================================

RATE_LIMITS = {
    "post_order": {"burst_10s": 3500, "sustained_10m": 36000},
    "post_orders_batch": {"burst_10s": 1000, "max_per_batch": 15},  # effective 15,000/10s
    "delete_order": {"burst_10s": 3000, "sustained_10m": 30000},
    "cancel_all": {"burst_10s": 250},
    "market_data_reads": {"burst_10s": 1500},
}

# =============================================================================
# PLATFORM TIMING
# =============================================================================

HEARTBEAT_INTERVAL_S = 5       # Send heartbeat every 5 seconds
HEARTBEAT_TIMEOUT_S = 10       # Server cancels all orders if missed
TUESDAY_RESTART_HOUR_ET = 7    # Matching engine restarts every Tuesday 7 AM ET
TUESDAY_RESTART_DURATION_S = 90  # ~90 seconds of downtime

# Dual-cadence monitoring (from weatherbot extraction)
DEFENSE_INTERVAL_S = 600       # Position monitoring every 10 minutes
OFFENSE_INTERVAL_S = 3600      # Market scanning every 60 minutes

# =============================================================================
# FEE STRUCTURE
# =============================================================================

# Makers pay 0% (and earn rewards)
# Takers: fee = C * feeRate * p * (1 - p)
FEE_RATES = {
    "crypto": 0.072,
    "sports": 0.03,
    "geopolitical": 0.0,  # exempt
}

# =============================================================================
# ICAO WEATHER STATIONS — 20 cities from weatherbot extraction
# =============================================================================
# Format: {slug: (icao_code, lat, lon, name, region, unit)}
# These coordinates match the EXACT airport stations Polymarket resolves on.
# Using city center coordinates instead introduces 3-8°F systematic error.

ICAO_STATIONS = {
    # US Cities
    "nyc":          ("KLGA", 40.7772, -73.8726, "New York City",  "us", "F"),
    "chicago":      ("KORD", 41.9742, -87.9073, "Chicago",        "us", "F"),
    "miami":        ("KMIA", 25.7959, -80.2870, "Miami",          "us", "F"),
    "dallas":       ("KDAL", 32.8471, -96.8518, "Dallas",         "us", "F"),
    "seattle":      ("KSEA", 47.4502, -122.3088, "Seattle",       "us", "F"),
    "atlanta":      ("KATL", 33.6407, -84.4277, "Atlanta",        "us", "F"),
    "denver":       ("KDEN", 39.8561, -104.6737, "Denver",        "us", "F"),
    "dc":           ("KDCA", 38.8512, -77.0402, "Washington DC",  "us", "F"),
    "la":           ("KLAX", 33.9425, -118.4081, "Los Angeles",   "us", "F"),
    "phoenix":      ("KPHX", 33.4373, -112.0078, "Phoenix",       "us", "F"),
    # Europe
    "london":       ("EGLC", 51.5053, 0.0553, "London",           "eu", "C"),
    "paris":        ("LFPG", 49.0097, 2.5478, "Paris",            "eu", "C"),
    "berlin":       ("EDDB", 52.3667, 13.5033, "Berlin",          "eu", "C"),
    "rome":         ("LIRF", 41.8003, 12.2389, "Rome",            "eu", "C"),
    # Asia
    "tokyo":        ("RJTT", 35.5494, 139.7798, "Tokyo",          "asia", "C"),
    "seoul":        ("RKSI", 37.4602, 126.4407, "Seoul",          "asia", "C"),
    "mumbai":       ("VABB", 19.0896, 72.8656, "Mumbai",          "asia", "C"),
    # South America
    "sao-paulo":    ("SBGR", -23.4356, -46.4731, "São Paulo",     "sa", "C"),
    # Oceania
    "sydney":       ("YSSY", -33.9461, 151.1772, "Sydney",        "oceania", "C"),
    "melbourne":    ("YMML", -37.6733, 144.8433, "Melbourne",     "oceania", "C"),
}

# US cities eligible for HRRR (CONUS coverage)
US_HRRR_CITIES = {slug for slug, data in ICAO_STATIONS.items() if data[4] == "us"}

# =============================================================================
# WEATHER API ENDPOINTS (all free, no API key except Visual Crossing)
# =============================================================================

OPEN_METEO_ECMWF_URL = "https://api.open-meteo.com/v1/ecmwf"
OPEN_METEO_HRRR_URL = "https://api.open-meteo.com/v1/gfs"
METAR_URL = "https://aviationweather.gov/api/data/metar"
VISUAL_CROSSING_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

# =============================================================================
# MONTHS (for Polymarket slug construction)
# =============================================================================

# =============================================================================
# SPORTSBOOK ODDS API (Phase 2 — Vegas Anchor strategy)
# =============================================================================

ODDSPAPI_URL = "https://api.oddspapi.io/v4"

# Sport keys for OddsPapi (priority order: widest Polymarket gaps first)
SPORT_KEYS = {
    "basketball_ncaab": "College Basketball",
    "basketball_nba": "NBA",
    "soccer_epl": "EPL",
    "soccer_uefa_champs": "Champions League",
    "mma_mixed_martial_arts": "MMA/UFC",
    "cricket_ipl": "IPL Cricket",
    "americanfootball_nfl": "NFL",
    "icehockey_nhl": "NHL",
    "baseball_mlb": "MLB",
}

# Fee drag by Polymarket category — edge must exceed this to be real
FEE_DRAG = {
    "sports": 0.0075,      # 0.75% taker fee at 50% probability
    "crypto": 0.018,       # 1.8% taker fee at 50% probability
    "politics": 0.01,      # 1.0%
    "weather": 0.0125,     # 1.25%
    "geopolitical": 0.0,   # Exempt
}

# =============================================================================
# MONTHS (for Polymarket slug construction)
# =============================================================================

MONTHS = [
    "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december",
]
