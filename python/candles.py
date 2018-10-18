import client
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import display as d

def initialize(path):
    df = pd.read_csv(path, index_col='symbol')
    return df

def display(df):
    for index, item in df.iterrows():
        # only do the PSEi for now_ts
        if(not item.psei):
            continue
        # retrieve history
        symbol = item.name

        equity = client.get_last(symbol, bars=3)
        print(symbol)
        # setup information
        equity['do'] = equity['open']
        equity['dh'] =  pd.Series(np.array([equity['high'].tail(3).max(), equity['high'].tail(2).max(), equity['high'].tail(1).max()]))
        equity['dl'] =  pd.Series(np.array([equity['low'].tail(3).min(), equity['low'].tail(2).min(), equity['low'].tail(1).min()]))
        equity['dc'] = pd.Series(np.repeat(equity.tail(1)['close'].values[0], 3))

        #normalize
        norm_equity = equity.drop(['date','volume','open','high','low','close'], axis=1)
        stripped_equity = equity.drop(['date','volume','do','dh','dl','dc'], axis=1)
        min = norm_equity['dl'].min()
        max = norm_equity['dh'].max()
        norm_equity = (norm_equity - min) / (max - min)
        d.plot(norm_equity)
# plot
# norm_equity.plot(marker='*',linestyle='--')
# stripped_equity.plot(marker='*',linestyle='--')
# plt.show()

equities = initialize(path='equities.csv')
display(equities)
