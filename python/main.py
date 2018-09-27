# import client
# import indicators
# import utils
# import pandas as pd
# import numpy as np
#
# final_string = "["
# stocks = ["GLO"]#
# company_name = ["GLO"] #,"AEV","AGI","ALI","AP","BDO","BPI","DMC","EDC","EMP","FGEN","GLO","GTCAP","ICT","JFC","LTG","MBT","MEG","MER","MPI","PCOR","RLC","SCC","SECB","SM","SMC","SMPH","TEL","URC"]
#
#
# for i, stock in enumerate(stocks):
#     dd = client.get_history(stock, convertTime=False, days=400)
#     dd = indicators.ema_close(dd)
#
#     dd["date"] = dd.date.apply(lambda x: x * 1000) # convert timestamp
#     dd = indicators.ac(dd)
#     dd = utils.get_signals(dd)
#
#
#     stock_id = "\"id\": \"{0}\"".format(stock)
#     stock_name = "\"name\": \"{0}\"".format(company_name[i])
#     stock_data =  "\"ohlc\": " + dd[["date","open","high","low","close"]].to_json(orient='values')
#     stock_combined = "{ " + stock_id + ", " + stock_name + ", " + stock_data + ","
#     stock_close = "\"close\": " + dd[dd["ema_close"] != 0][["date","ema_close"]].to_json(orient='values') + ","
#     indicator_ac = "\"ac\": " + dd[["date","ac"]].to_json(orient='values') + ","
#     signal = "\"signal\": " + dd[dd["signal"] != 0][["date","signal"]].to_json(orient='values')
#     final_string = final_string + stock_combined + stock_close + indicator_ac + signal + "}"
#
#     if i < len(stocks) - 1:
#         final_string = final_string + ", "
#
# final_string = final_string + "]"
#
# print(final_string)
# %%
import client
import indicators
import matplotlib.pyplot as plt
import pandas as pd


# %%
stocks = ["AC","AEV","AGI","ALI","AP","BDO","BPI","DMC","EDC","EMP","FGEN","GLO","GTCAP","ICT","JFC","LTG","MBT","MEG","MER","MPI","PCOR","RLC","SCC","SECB","SM","SMC","SMPH","TEL","URC"]
for stock in stocks:
    # print("Checking %s" % stock)
    df = client.get_history(stock)
    df = indicators.relative_strength_index(df)
    df = indicators.ema_rsi(df)

    df_norm = df[['ema_rsi', 'rsi']]
    # df_norm = (df_norm - 0.50) * 2 * 100
    ema_rsi = df_norm['ema_rsi'] # .rolling(window=5, win_type='gaussian', center=True).mean(std=3)
    ema_rsi = (ema_rsi - 0.5)
    ema_rsi = ema_rsi * 100
    ema_rsi = ema_rsi.rolling(window=5, win_type='gaussian', center=True).mean(std=3)
    ema_rsi = ema_rsi.shift(2)

    rsi = df['rsi']
    rsi = (rsi - 0.5) * 100

    close = df['close']
    close = (((close - close.min()) / (close.max() - close.min()))) * 100
    close_smoothed = close.rolling(window=5, win_type='gaussian', center=True).mean(std=3)

    if(ema_rsi.iloc[-1] > 0):
        plt.figure(figsize=(20,4))
        # rsi.plot(legend=True, title=stock)
        ema_rsi.tail(20).plot(legend=True)
        close_smoothed.tail(20).plot(legend=True)
        plt.axhline(y=0, color='black', linestyle='--')
        plt.show()
# close.plot()
# close_smoothed.plot()
# plt.figure()
# plt.show()


#
# import pymongo
# from pymongo import MongoClient
# import os
#
# # username = os.environ["mongo_username"]
# # password = os.environ["mongo_password"]
# username = "admin-monkey"
# password = "admin-monkey123"
#
# print("Connecting to mLab with username: %s" % username)
# client = MongoClient("mongodb://%s:%s@ds231360.mlab.com:31360" % (username, password))
#
# db = client.quantmonkey
# rec = db.recommendations
#
# rec.insert_one({'a':1})
