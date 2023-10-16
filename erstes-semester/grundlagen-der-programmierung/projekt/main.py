"""File contains the main code"""
from helpers.dbconnection import dbcon

db = dbcon()

print(db.gdp_project.test_collection.find_one({}))
