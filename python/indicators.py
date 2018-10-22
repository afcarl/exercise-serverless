import pandas as pd
from collections import namedtuple

def ema(df, column_in, column_out, n=20):
    ema = pd.Series(df[column_in].ewm(span=n, min_periods=n).mean(), name=column_out)
    df = df.join(ema)
    return df

def ema_rsi(df, n=20):
    ema = pd.Series(df['rsi'].ewm(span=n, min_periods=n).mean(), name='ema_rsi')
    df = df.join(ema)
    return df

def day_range_pct(df):
    drp = pd.Series(((df['high'] - df['low']) / df['close']) * 100, name='day_range_pct')
    df = df.join(drp)
    return df

def day_range_pct(df):
    drp = pd.Series(((df['high'] - df['low']) / df['close']) * 100, name='day_range_pct')
    df = df.join(drp)
    return df

def relative_strength_index(df, n=14):
    i = 0
    up_index = [0]
    down_index = [0]
    while i + 1 <= df.index[-1]:
        up_move = df.loc[i + 1, 'high'] - df.loc[i, 'high']
        down_move = df.loc[i, 'low'] - df.loc[i + 1, 'low']
        if up_move > down_move and up_move > 0:
            up_d = up_move
        else:
            up_d = 0
        up_index.append(up_d)
        if down_move > up_move and down_move > 0:
            dod = down_move
        else:
            dod = 0
        down_index.append(dod)
        i = i + 1
    up_index = pd.Series(up_index)
    down_index = pd.Series(down_index)
    positive_di = pd.Series(up_index.ewm(span=n, min_periods=n).mean())
    negative_di = pd.Series(down_index.ewm(span=n, min_periods=n).mean())
    rsi = pd.Series(positive_di / (positive_di + negative_di), name='rsi')
    df = df.join(rsi)
    return df

def heiken_ashi(df):
    df['ha_close'] = (df['open'] + df['high'] + df['low'] + df['close']) / 4
    nt = namedtuple('nt', ['open','close'])
    previous_row = nt(df.loc[0,'open'],df.loc[0,'close'])
    i = 0
    for row in df.itertuples():
        ha_open = (previous_row.open + previous_row.close) / 2
        df.loc[i,'ha_open'] = ha_open
        previous_row = nt(ha_open, row.close)
        i += 1

    df['ha_high'] = df[['ha_open','ha_close','high']].max(axis=1)
    df['ha_low'] = df[['ha_open','ha_close','low']].min(axis=1)
    return df
