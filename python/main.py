import utils
utils.print_signals()

# import pymongo
# from pymongo import MongoClient
# import os
#
# username = os.environ["mongo_username"]
# password = os.environ["mongo_password"]
#
# print("Connecting to mLab with username: %s" % username)
# client = MongoClient("mongodb://%s:%s@ds231360.mlab.com:31360" % (username, password))
#
# db = client.quantmonkey
# rec = db.recommendations
#
# rec.find({})
