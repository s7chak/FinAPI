hero_snap_months=6
hero_lines_file = "dt/market_lines_cache.json"
yfin_delay_sec=1.5
scai_palette_bg_1 = '#0a0d14'

market_metadata = {
    "S&P500": {
        "name": "S&P 500",
        "symbol": "^GSPC",
        "color": "blue",
        "type": ["US Equities","International Equities","Emerging Markets", "Europe"]
    },
    "DowJones": {
        "name": "Dow Jones Industrial Average",
        "symbol": "^DJI",
        "color": "white",
        "type": "US Equities"
    },
    "Russell2000": {
        "name": "Russell 2000",
        "symbol": "^RUT",
        "color": "teal",
        "type": "US Equities"
    },
    "VIX": {
        "name": "S&P 500 Volatility Index",
        "symbol": "^VIX",
        "color": "purple",
        "type": "US Macro"
    },
    "Treasury2Y": {
        "name": "US 2Y Treasury Yield",
        "symbol": "^IRX",
        "color": "lightgray",
        "type": "US Macro"
    },
    "Treasury10Y": {
        "name": "US 10Y Treasury Yield",
        "symbol": "^TNX",
        "color": "gray",
        "type": "US Macro"
    },
    # "GDP": {
    #     "name": "US Gross Domestic Product",
    #     "symbol": "GDP",
    #     "color": "teal",
    #     "type": "US Macro"
    # },
    # "Unemployment": {
    #     "name": "US Unemployment Rate",
    #     "symbol": "UNRATE",
    #     "color": "orange",
    #     "type": "US Macro"
    # },
    # "CPI": {
    #     "name": "US Consumer Price Index",
    #     "symbol": "CPI",
    #     "color": "red",
    #     "type": "US Macro"
    # },
    # "FedFunds": {
    #     "name": "Federal Funds Rate",
    #     "symbol": "FEDFUNDS",
    #     "color": "gold",
    #     "type": "US Macro"
    # },
    # "PrimeRate": {
    #     "name": "US Prime Rate",
    #     "symbol": "MPRIME",
    #     "color": "pink",
    #     "type": "US Macro"
    # },
    "Gold": {
        "name": "Gold",
        "symbol": "GC=F",
        "color": "gold",
        "type": "US Equities"
    },
    "Oil": {
        "name": "Crude Oil (WTI)",
        "symbol": "CL=F",
        "color": "brown",
        "type": "US Equities"
    },
    "Bitcoin": {
        "name": "Bitcoin",
        "symbol": "BTC-USD",
        "color": "darkgreen",
        "type": "US Equities"
    },
    "FTSE100": {
        "name": "FTSE 100",
        "symbol": "^FTSE",
        "color": "darkred",
        "type": "International Equities"
    },
    "EmergingMarkets": {
        "name": "MSCI Emerging Markets",
        "symbol": "EEM",
        "color": "yellow",
        "type": "Emerging Markets"
    },
    "DAX": {
        "name": "DAX",
        "symbol": "^GDAXI",
        "color": "darkorange",
        "type": "International Equities"
    },
    "Nikkei225": {
        "name": "Nikkei 225",
        "symbol": "^N225",
        "color": "darkcyan",
        "type": "International Equities"
    },
    "HangSeng": {
        "name": "Hang Seng",
        "symbol": "^HSI",
        "color": "darkmagenta",
        "type": "International Equities"
    },
    "SENSEX": {
        "name": "BSE Sensex",
        "symbol": "^BSESN",
        "color": "gold",
        "type": "International Equities"
    },
    "EuroStoxx50": {
        "name": "Euro Stoxx 50",
        "symbol": "^STOXX50E",
        "color": "pink",
        "type": "International Equities"
    },
    "USDollarIndex": {
        "name": "US Dollar Index",
        "symbol": "DX-Y.NYB",
        "color": "red",
        "type": "FX"
    },
    "EURUSD": {
        "name": "EUR/USD",
        "symbol": "EURUSD=X",
        "color": "lightblue",
        "type": "FX"
    },
    "INRUSD": {
        "name": "INR/USD",
        "symbol": "INRUSD=X",
        "color": "green",
        "type": "FX"
    }
}
