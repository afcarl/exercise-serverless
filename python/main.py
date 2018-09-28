import client
import indicators
import utils

import pandas as pd
import numpy as np

import os
import requests
import re

equities = pd.read_csv('equities.csv', index_col='symbol')

equities['strength_index'] = pd.Series()
equities['price'] = pd.Series()
equities['norm_close'] = pd.Series()

for index, equity in equities.iterrows():

    # only do the PSEi for now_ts
    if(not equity.psei):
        continue

    # retrieve history
    symbol = equity.name
    equity = client.get_history(symbol, days=400)

    # calculate the indicators
    equity = indicators.relative_strength_index(equity, n=14)
    equity = indicators.ema_rsi(equity, n=30)

    # normalize and smoothen
    equity['norm_ema_rsi'] = (equity['ema_rsi'] - 0.5) * 200
    equity['norm_close'] = ((equity['close'] - equity['close'].min()) / (equity['close'].max() - equity['close'].min())) * 100
    equity['smoothed_close'] = equity['norm_close'].rolling(
        window=5,
        win_type='gaussian',
        center=True).mean(std=3).shift(2)

    # remove all NA -- cleanup
    # not really neccessary...
    # equity = equity.dropna()
    # just take last 200 rows
    # equity = equity.tail(200)
    # equity.reset_index(drop=True, inplace=True)

    # add to equities dataframe
    equities.loc[symbol,'strength_index'] = equity['norm_ema_rsi'].tail(1).values
    equities.loc[symbol,'price'] = equity['close'].tail(1).values
    equities.loc[symbol,'norm_close'] = equity['norm_close'].tail(1).values

# make the symbol a column
equities.reset_index(level=0, inplace=True)

# FIX ME JSON PROBLEM
json = [dict([(colname, row[i]) for i, colname in enumerate(equities.columns)])
    for row in equities.values ]


# url = 'https://api.jsonbin.io/b/5badfc4d8713b17b52b0b603'
# key = os.environ['JSONBIN_KEY']
# headers = {'secret-key': key}
# response = requests.put(url, json=json, headers=headers).json()
# print(response)
