import pymongo
import pandas as pd

client = pymongo.MongoClient()
db = client.iris
db.iris.update_many({'Species': 'Iris-setosa'}, {'$inc':{'SepalLengthCm': -1}})
