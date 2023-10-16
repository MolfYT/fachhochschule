"""This file contains the DB connection"""
import os
from pymongo import MongoClient

def dbcon():
    """This function establishes a connection to MongoDB"""

    if os.environ["CODESPACES"]:
        mongo_db_secret = os.environ["MONGODB_FH_SECRET"]
    else:
        mongo_db_secret = "your secret"

    # Connect to DB
    db = MongoClient(mongo_db_secret)

    return db
