from flask_cors import CORS, cross_origin
import finutil as util
import pandas as pd
from flask import Flask, jsonify, make_response, request
import os, json
import finapi_config as config

app = Flask(__name__)
CORS(app)
CACHE_FILE = config.hero_lines_file
f_months = config.hero_snap_months
f_delay = config.yfin_delay_sec

def get_market_lines_data():
    try:
        if os.path.exists(CACHE_FILE):
            data = json.load(open(CACHE_FILE))
            df = pd.DataFrame({k: pd.Series(v) for k, v in data.items()})
            df.index = pd.to_datetime(df.index)
            return df
    except: raise
    data = util.get_market_lines(f_delay, months=f_months)
    try: json.dump(data, open(CACHE_FILE, "w"), indent=2)
    except: raise
    df = pd.DataFrame({k: pd.Series(v) for k, v in data.items()})
    df.index = pd.to_datetime(df.index)
    return df

@app.route("/api/market-lines-data")
def market_lines_data():
    return jsonify(get_market_lines_data().to_dict())

@app.route("/api/market-lines", methods=['GET'])
@cross_origin()
def market_lines():
    try:
        req_type = request.args.get("type", "US Equities")
        df = get_market_lines_data()
        _, plot_data = util.make_market_plot(df, req_type)
        print(f"Summary plot data done: {req_type}")
        return make_response({'plot': plot_data}, 200)
    except Exception as e:
        print(str(e))
        return make_response(jsonify({"error": str(e)}), 500)

@app.route("/")
def home_finapi():
    return "FinAPI running for scaiverse: v1.0"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 1000))  # Default to 8080 if PORT is not set
    app.run(host="0.0.0.0", port=port)
