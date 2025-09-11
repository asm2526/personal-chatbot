"""
Intent API routes.
Provides full CRUD (Create, Read, Update, Delete) functionality
for chatbot intents stored in MongoDB"""

from fastapi import APIRouter, HTTPException
from typing import List
from src.models.intent import Intent
from src.core.database import get_collection

router = APIRouter()
collection = get_collection("intents")

#Create intent
@router.post("/intent", response_model=dict)
def add_intent(intent: Intent):
    """
    Endpoint: POST /api/intent
    Add a new intent to the dtsbse"""
    if not intent.intent.strip() or not intent.responses:
        raise HTTPException(status_code=400, detail="Intent and responses are required")
    collection.insert_one(intent.dict())
    return {"message": "Intent added successfully"}

# get single intent by name
@router.get("/intent/{intent_name}", response_model=Intent | dict)
def get_intent(intent_name: str):
    """
    Endpoint: GET /api/intent/{intent_name}
    Fetch a single intent by name
    """
    intent = collection.find_one({"intent": intent_name}, {"_id": 0})
    if not intent:
        raise HTTPException(status_code=404, detail="Intent not found")
    return intent

# list all intents
@router.get("/intent", response_model=List[Intent])
def list_intents():
    """
    Endpoint: GET /api/intent
    Fetch all intents in the database
    """
    intents = list(collection.find({}, {"_id": 0}))
    return intents

# update intent by name
@router.put("/intent/{intent_name}", response_model=dict)
def update_intent(intent_name: str, intent: Intent):
    """
    Endpoint: PUT /api/intent/{intent_name}
    Update an existing intent by replcaing its responses
    """
    result = collection.update_one({"intent": intent_name}, {"$set": intent.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Intent not found")
    return {"message": "Intent updated successfully"}

# Delete intent by name
@router.delete("/intent/{intent_name}", response_model=dict)
def delete_intent(intent_name: str):
    """
    Endpoint: DELETE /api/intent/{intent_name}
    Delete an intent from the database by name
    """
    result = collection.delete_one({"intent": intent_name})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Intent not found")
    return {"message": "Intent deleted successfully"}
    