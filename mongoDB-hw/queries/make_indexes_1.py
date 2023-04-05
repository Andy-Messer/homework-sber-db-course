import pymongo
import pandas as pd

client = pymongo.MongoClient()
db = client.iris

db.iris.create_index([('Species', pymongo.DESCENDING)])
db.iris.create_index([('SepalLengthCm', pymongo.DESCENDING)])
