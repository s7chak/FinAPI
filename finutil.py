import json
import time
from datetime import datetime
import plotly.graph_objects as go
import plotly.io as pio

import pandas as pd
import yfinance as yf
import finapi_config as config


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
