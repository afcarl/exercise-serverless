import pandas as pd

def ema_rsi(df, n=20):
    ema = pd.Series(df['rsi'].ewm(span=n, min_periods=n).mean(), name='ema_rsi')
    df = df.join(ema)
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
