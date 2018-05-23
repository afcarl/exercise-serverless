import pandas as pd
from collections import namedtuple
import indicators
import client

# get buy signals
def get_signals(df):
    # start at 2 cause we need at least 2 days prior to test
    for i in range(2, df.shape[0]):
        ac = df.loc[i-2:i,"ac"].values # ac 2 days ago to now
        if ac[0] < 0 and ac[1] < 0 and ac[0] < ac[1] and ac[1] < ac[2] and ac[2] > 0:
            df.loc[i,"signal"] = 1
        elif ac[0] > 0 and ac[1] > 0 and ac[0] > ac[1] and ac[1] > ac[2] and ac[2] < 0:
            df.loc[i,"signal"] = -1
        else:
            df.loc[i,"signal"] = 0
        i += 1
    df = df.fillna(0)
    return df

def print_signals():
    stocks = ["AC","AEV","AGI","ALI","AP","BDO","BPI","DMC","EDC","EMP","FGEN","GLO","GTCAP","ICT","JFC","LTG","MBT","MEG","MER","MPI","PCOR","RLC","SCC","SECB","SM","SMC","SMPH","TEL","URC"]
    for stock in stocks:
        dd = client.get_history(stock)
        dd = indicators.ac(dd)
        dd = get_signals(dd)
        if(dd.signal.iloc[-1] != 0):
            print(stock)
            print(dd.tail())
            print("\n")

# rec.insert_many([
#     {"item": "journal",
#      "qty": 25,
#      "size": {"h": 14, "w": 21, "uom": "cm"},
#      "status": "A"},
#     {"item": "notebook",
#      "qty": 50,
#      "size": {"h": 8.5, "w": 11, "uom": "in"},
#      "status": "A"},
#     {"item": "paper",
#      "qty": 100,
#      "size": {"h": 8.5, "w": 11, "uom": "in"},
#      "status": "D"},
#     {"item": "planner",
#      "qty": 75, "size": {"h": 22.85, "w": 30, "uom": "cm"},
#      "status": "D"},
#     {"item": "postcard",
#      "qty": 45,
#      "size": {"h": 10, "w": 15.25, "uom": "cm"},
#      "status": "A"}])
