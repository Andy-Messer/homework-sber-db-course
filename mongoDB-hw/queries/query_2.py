import pymongo
import pandas as pd

client = pymongo.MongoClient()
db = client.iris

x = db.iris.delete_many({'Species': 'Iris-versicolor'})
print(x.deleted_count, " documents deleted.")
