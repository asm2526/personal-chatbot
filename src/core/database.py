import os
from pymongo import MongoClient
from dotenv import load_dotenv

# load environment variables from .env
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "chatbot")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]

def get_collection(name: str):
    return db[name]