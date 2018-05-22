import pymongo
from pymongo import MongoClient
import os

username = os.environ["mongo_username"]
password = os.environ["mongo_password"]

print("Connecting to mLab with username: %s" % username)
client = MongoClient("mongodb://%s:%s@ds231360.mlab.com:31360" % (username, password))

db = client.quantmonkey
rec = db.recommendations

rec.find({})


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
