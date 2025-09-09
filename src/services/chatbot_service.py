from src.core.database import get_collection
import random

collection = get_collection("intents")

def get_reply(user_message: str) -> str:
    #match intent by exact name for now
    intent = collection.find_one({"intent": user_message.lower()}, {"_id": 0})

    if intent:
        return random.choice(intent["responses"])
    else:
        return "I don't understand yet"