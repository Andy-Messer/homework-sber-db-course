import pymongo
import pandas as pd

client = pymongo.MongoClient()
db = client.iris
df = pd.read_csv('Iris.csv')
db.iris.insert_many(df.to_dict('records'))
