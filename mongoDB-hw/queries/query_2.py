import pymongo
import pandas as pd

client = pymongo.MongoClient()
db = client.iris
print(client.getCollectionNames())