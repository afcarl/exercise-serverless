import matplotlib.pyplot as plt

def create_json(df):
    json = [dict([(colname, row[i]) for i, colname in enumerate(df.columns)])
        for row in df.values ]
    return json

def plot(df):
    # plot
    plt.figure(figsize=(5,2))
    df.norm_ema_rsi.plot(legend=True, title=df.symbol)
    df.smoothed_close.plot(legend=True)
    plt.axhline(y=0, color='black', linestyle='--', alpha=0.2)
    plt.annotate('%0.2f' % df.norm_ema_rsi.tail(1),
        xy=(1, df.norm_ema_rsi.tail(1)),
        xytext=(8, 0),
        xycoords=('axes fraction', 'data'),
        textcoords='offset points')
    plt.ylim([-100,100])
    plt.show()
