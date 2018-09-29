import client
import indicators
import utils

import pandas as pd

def initialize(path):
    df = pd.read_csv(path, index_col='symbol')
    df['strength_index'] = pd.Series()
    df['price'] = pd.Series()
    df['norm_close'] = pd.Series()
    return df

def populate(df):
    for index, item in df.iterrows():
        # only do the PSEi for now_ts
        if(not item.psei):
            continue

        # retrieve history
        symbol = item.name
        item = client.get_history(symbol, days=400)

        # calculate the indicators
        item = indicators.relative_strength_index(item, n=14)
        item = indicators.ema_rsi(item, n=30)

        # normalize and smoothen
        item['norm_ema_rsi'] = (item['ema_rsi'] - 0.5) * 200
        item['norm_close'] = ((item['close'] - item['close'].min()) /
            (item['close'].max() - item['close'].min())) * 100
        item['smoothed_close'] = item['norm_close'].rolling(
            window=5,
            win_type='gaussian',
            center=True).mean(std=3).shift(2)

        # remove all NA -- cleanup
        # not really neccessary...
        # item = item.dropna()
        # just take last 200 rows
        # item = item.tail(200)
        # item.reset_index(drop=True, inplace=True)

        # add to df dataframe
        df.loc[symbol,'strength_index'] = item['norm_ema_rsi'].tail(1).values
        df.loc[symbol,'price'] = item['close'].tail(1).values
        df.loc[symbol,'norm_close'] = item['norm_close'].tail(1).values

    df.reset_index(inplace=True)
    df = df.dropna()
    return df

# actual code
equities = initialize(path='equities.csv')
equities = populate(equities)
json = utils.create_json(equities)
print(client.put_json(json))
