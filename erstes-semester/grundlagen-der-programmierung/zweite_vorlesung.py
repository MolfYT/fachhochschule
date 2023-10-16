"""File contains code from the second lecture"""
import os
from pymongo import MongoClient

MONGO_DB_SECRET = os.environ["MONGODB_FH_SECRET"]

# Connect to DB
db = MongoClient(MONGO_DB_SECRET)

print(db.fh.test_collection.find_one({}))
