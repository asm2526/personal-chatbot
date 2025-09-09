from fastapi import APIRouter
from typing import List
from src.models.intent import Intent
from src.core.database import get_collection

router = APIRouter()
collection = get_collection("intents")

#Create intent
@router.post("/intent")
def add_intent(intent: Intent):
    collection.insert_one(intent.dict())
    return {"message": "Intent added successfully"}

# get single intent by name
@router.get("/intent/{intent_name}")
def get_intent(intent_name: str):
    intent = collection.find_one({"intent": intent_name}, {"_id": 0})
    if not intent:
        return {"message": "Intent not found"}
    return intent

# list all intents
@router.get("/intent")
def list_intents():
    intents = list(collection.find({}, {"_id": 0}))
    return intents

# update intent by name
@router.put("/intent")
def update_intent(intent_name: str, intent: Intent):
    result = collection.update_one({"intent": intent_name}, {"$set": intent.dict()})
    if result.matched_count == 0:
        return {"message": "Intent not found"}
    return {"message": "Intent updated successfully"}

# Delete intent by name
@router.delete("/intent/{intent_name}")
def delete_invent(intent_name: str):
    result = collection.delete_one({"intent": intent_name})
    if result.deleted_count == 0:
        return {"message": "Intent not found"}
    return {"message": "Intent delete succesfully"}
