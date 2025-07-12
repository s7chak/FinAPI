import json
import time
from datetime import datetime
import plotly.graph_objects as go
import plotly.io as pio

import pandas as pd
import yfinance as yf
import finapi_config as config
from fin_objects import Stock

def get_market_lines(delay_sec=1.5, months=6):
    end_date = datetime.today()
    start_date = end_date - pd.DateOffset(months=months)
    data = {}
    market_metadata = config.market_metadata
    tickers = {k: v["symbol"] for k, v in market_metadata.items()}
    for name, symbol in tickers.items():
        try:
            print(f"Fetching {name} ({symbol}) …")
            ticker = yf.Ticker(symbol)
            hist = ticker.history(start=start_date.strftime("%Y-%m-%d"), end=end_date.strftime("%Y-%m-%d"))
            if hist.empty or 'Close' not in hist:
                print(f"Warning: No data for {symbol}")
                continue
            series = hist['Close'].dropna()
            data[name] = {str(date.date()): round(value, 4) for date, value in series.items()}
            time.sleep(delay_sec)
        except Exception as e:
            print(f"Error fetching {symbol}: {e}")
            continue
    return data


def make_market_plot(df, req_type):
    market_metadata = config.market_metadata
    colors = {k: v["color"] for k, v in market_metadata.items()}
    types = {k: v["type"] for k, v in market_metadata.items()}
    cols = [col for col in df.columns if req_type in (types.get(col) if isinstance(types.get(col), list) else [types.get(col)])]
    df = df.apply(lambda s: s / s.dropna().iloc[0])
    fig = go.Figure(
        data=[
            go.Scatter(
                x=df.index,
                y=df[col],
                mode='lines',
                name=col,
                line=dict(dash='solid', color=colors.get(col)),
                connectgaps=True
            )
            for col in cols
        ],
        layout=dict(
            title_text=req_type,
            paper_bgcolor=config.scai_palette_bg_1,
            plot_bgcolor=config.scai_palette_bg_1,
            font_color="#fff",
            xaxis_showgrid=False,
            yaxis_showgrid=False
        )
    )
    return fig, json.loads(pio.to_json(fig))


def stock_analysis_init(ticker):
    def safe_get(key):
        return info[key] if key in info else None
    stock = Stock()
    stock.ticker = ticker
    try:
        yf_ticker = yf.Ticker(ticker)
        info = yf_ticker.info
        if "currentPrice" not in info:
            raise Exception("No latest price information, symbol might be delisted.")
    except Exception as e:
        raise e
    stock.company_name = safe_get("longName") or safe_get("shortName")
    stock.current_price = safe_get("currentPrice")
    stock.market_cap = human_readable_number(safe_get("marketCap"))
    stock.enterprise_value = human_readable_number(safe_get("enterpriseValue"))
    stock.shares_outstanding = human_readable_number(safe_get("sharesOutstanding"))
    stock.pe_ratio_ttm = safe_get("trailingPE")
    stock.pe_ratio_forward = safe_get("forwardPE")
    stock.peg_ratio = safe_get("pegRatio")
    stock.pb_ratio = safe_get("priceToBook")
    stock.ps_ratio = safe_get("priceToSalesTrailing12Months")
    stock.ev_ebitda = safe_get("enterpriseToEbitda")
    stock.eps_ttm = safe_get("trailingEps")
    stock.eps_forward = safe_get("forwardEps")
    stock.revenue_ttm = human_readable_number(safe_get("totalRevenue"))
    stock.net_income = human_readable_number(safe_get("netIncomeToCommon"))
    stock.gross_margin = safe_get("grossMargins")
    stock.operating_margin = safe_get("operatingMargins")
    stock.roe = safe_get("returnOnEquity")
    stock.roa = safe_get("returnOnAssets")
    stock.debt_to_equity = safe_get("debtToEquity")
    stock.current_ratio = safe_get("currentRatio")
    stock.quick_ratio = safe_get("quickRatio")
    stock.dividend_yield = safe_get("dividendYield")
    stock.dividend_rate = safe_get("dividendRate")
    # stock.ex_dividend_date = safe_get("exDividendDate")
    stock.payout_ratio = safe_get("payoutRatio")
    stock.beta = safe_get("beta")
    stock.fifty_two_week_high = safe_get("fiftyTwoWeekHigh")
    stock.fifty_two_week_low = safe_get("fiftyTwoWeekLow")
    stock.one_year_target = safe_get("targetMeanPrice")
    # stock.earnings_date = yf_ticker.calendar if yf_ticker.calendar is not None else None
    stock.sector = safe_get("sector")
    stock.industry = safe_get("industry")
    stock.employees = safe_get("fullTimeEmployees")

    return stock.to_dict()