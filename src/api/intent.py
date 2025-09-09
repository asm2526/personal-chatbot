from fastapi import APIRouter
from src.models.intent import Intent
from src.core.database import get_collection

router = APIRouter()
collection = get_collection("intents")

@router.post("/intent")
def add_intent(intent: Intent):
    collection.insert_one(intent.dict())
    return {"message": "Intent added successfully"}

@router.get("/intent/{intent_name}")
def get_intent(intent_name: str):
    intent = collection.find_one({"intent": intent_name}, {"_id": 0})
    if not intent:
        return {"message": "Intent not found"}
    return intent