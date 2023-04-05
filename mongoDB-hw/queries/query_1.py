import pymongo
import pandas as pd

client = pymongo.MongoClient()
db = client.iris
query = db.test.find({'Species': 'Iris-setosa'}).sort('SepalLengthCm', 1).limit(1)
for x in query:
    print(x)

q = db.test.find({'Species': 'Iris-setosa'}).sort('SepalLengthCm', 1).limit(1).explain()['executionStats']
print(q)