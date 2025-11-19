#---------------------------------------
# MongoDB connection
#---------------------------------------
# Provides a reusable function to establish a connection to MongoDB
# using the URI stored securely in config.py (loaded from .env).
# Returns both the collection object and the client object.
# Note: The client must be closed after use to free resources.

import pymongo
from config import MONGO_URI

def get_mongo_collection(db,collection):
    client=pymongo.MongoClient(MONGO_URI)
    db=client[db]
    return db[collection],client