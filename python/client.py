import pandas as pd
import requests
from datetime import datetime, timedelta
import os

def get_history(symbol, convertTime=True, days=100):
    now = datetime.today()
    past = now - timedelta(days)
    now_ts = str(int(now.timestamp()))
    past_ts = str(int(past.timestamp()))

    url = "http://api.pse.tools/api/chart/history?symbol={0}&resolution=D&from={1}&to={2}".format(symbol, past_ts, now_ts)
    response = requests.get(url).json()
    result = pd.Series()
    if response["s"] == "ok":
        time_series  = pd.Series(response["t"], name="date")
        open_series  = pd.Series(response["o"], name="open")
        high_series = pd.Series(response["h"], name="high")
        low_series   = pd.Series(response["l"], name="low")
        close_series = pd.Series(response["c"], name="close")
        volume_series = pd.Series(response["v"], name="volume")

        result = pd.concat([time_series, open_series, high_series, low_series, close_series, volume_series], axis=1)

        if convertTime:
            result.date = result.date.apply(convert_unix_time)
    return result

def convert_unix_time(date):
    d = datetime.fromtimestamp(date)
    day = str(d.day)
    month = str(d.month)
    year = str(d.year)
    return "{0}-{1}-{2}".format(year, month.zfill(2), day.zfill(2))

def post_json():
    url = 'https://api.jsonbin.io/b/5badfc4d8713b17b52b0b603'
    key = os.environ['JSONBIN_KEY']
    headers = {'secret-key': key}

    req = requests.put(url, json=nil, headers=headers)
    print(req.text)
