"""
Database connection utility.
This module connects to MongoDB and exposes a helper function
to access collections inside the chosen database
"""

import os
from pymongo import MongoClient
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# get mongoDB connection URI and DB name from environment
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "chatbot")

# Create a MongoDB client
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]

def get_collection(name: str):
    """
    Return a reference to a MongoDB collection by name.
    Example: get_collection("intents")"""
    return db[name]
