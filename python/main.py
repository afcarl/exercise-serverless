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


    stock_id = "\"id\": \"{0}\"".format(stock)
    stock_name = "\"name\": \"{0}\"".format(company_name[i])
    stock_data =  "\"ohlc\": " + dd[["date","open","high","low","close"]].to_json(orient='values')
    stock_combined = "{ " + stock_id + ", " + stock_name + ", " + stock_data + ","
    stock_close = "\"close\": " + dd[dd["ema_close"] != 0][["date","ema_close"]].to_json(orient='values') + ","
    indicator_ac = "\"ac\": " + dd[["date","ac"]].to_json(orient='values') + ","
    signal = "\"signal\": " + dd[dd["signal"] != 0][["date","signal"]].to_json(orient='values')
    final_string = final_string + stock_combined + stock_close + indicator_ac + signal + "}"

    if i < len(stocks) - 1:
        final_string = final_string + ", "

final_string = final_string + "]"

print(final_string)

# import client
# import indicators
# import matplotlib.pyplot as plt
#
# df = client.get_history("SMPH", days=300)
# df = indicators.previous_close(df)
#
# df
#
# df['previous_close'].std()
# df['previous_close'].mean()
# df['previous_close'].plot.hist(alpha=0.5, bins=50)
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
