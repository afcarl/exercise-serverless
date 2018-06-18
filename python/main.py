
import client

final_string = "["
stocks = ["AC","AEV","AGI","ALI","AP","BDO","BPI","DMC","EDC","EMP","FGEN","GLO","GTCAP","ICT","JFC","LTG","MBT","MEG","MER","MPI","PCOR","RLC","SCC","SECB","SM","SMC","SMPH","TEL","URC"]
company_name = ["AC","AEV","AGI","ALI","AP","BDO","BPI","DMC","EDC","EMP","FGEN","GLO","GTCAP","ICT","JFC","LTG","MBT","MEG","MER","MPI","PCOR","RLC","SCC","SECB","SM","SMC","SMPH","TEL","URC"]
#,"AEV","AGI","ALI","AP","BDO","BPI","DMC","EDC","EMP","FGEN","GLO","GTCAP","ICT","JFC","LTG","MBT","MEG","MER","MPI","PCOR","RLC","SCC","SECB","SM","SMC","SMPH","TEL","URC"]
for i, stock in enumerate(stocks):
    dd = client.get_history(stock, convertTime=False, days=1000)
    dd["date"] = dd.date.apply(lambda x: x * 1000) # convert timestamp
    # dd = dd.drop(['volume'], axis=1)
    # dd = dd.rename(columns={'date': 'y'})
    stock_id = "\"id\": \"{0}\"".format(stock)
    stock_name = "\"name\": \"{0}\"".format(company_name[i])
    stock_data =  "\"data\": " + dd.to_json(orient='values')
    stock_combined = "{ " + stock_id + ", " + stock_name + ", " + stock_data + " }"
    final_string = final_string + stock_combined
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
