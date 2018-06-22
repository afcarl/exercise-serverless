import client
import indicators
import utils
import pandas as pd
import numpy as np

final_string = "["
stocks = ["GLO"]#
company_name = ["GLO"] #,"AEV","AGI","ALI","AP","BDO","BPI","DMC","EDC","EMP","FGEN","GLO","GTCAP","ICT","JFC","LTG","MBT","MEG","MER","MPI","PCOR","RLC","SCC","SECB","SM","SMC","SMPH","TEL","URC"]


for i, stock in enumerate(stocks):
    dd = client.get_history(stock, convertTime=False, days=400)
    dd = indicators.ema_close(dd)

    dd["date"] = dd.date.apply(lambda x: x * 1000) # convert timestamp
    dd = indicators.ac(dd)
    dd = utils.get_signals(dd)
    dd['signal_buy'] = np.where(dd['signal'] == 1, "Buy", 0)
    dd['signal_sell'] = np.where(dd['signal'] == -1, "Sell", 0)

    stock_id = "\"id\": \"{0}\"".format(stock)
    stock_name = "\"name\": \"{0}\"".format(company_name[i])
    stock_data =  "\"ohlc\": " + dd[["date","open","high","low","close"]].to_json(orient='values')
    stock_combined = "{ " + stock_id + ", " + stock_name + ", " + stock_data + ","
    stock_close = "\"close\": " + dd[["date","ema_close"]].to_json(orient='values') + ","
    indicator_ac = "\"ac\": " + dd[["date","ac"]].to_json(orient='values') # + ","
    # signal = "\"signal\": " + dd[["date","signal_buy"]].to_json(orient='values')
    final_string = final_string + stock_combined + stock_close + indicator_ac + "}"

    if i < len(stocks) - 1:
        final_string = final_string + ", "

final_string = final_string + "]"

print(final_string)
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
