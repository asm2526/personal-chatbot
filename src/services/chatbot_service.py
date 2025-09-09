"""
Chatbot service logic
handles message processing and returns appropriate replies
based ons tored intents in MongoDB
"""

from src.core.database import get_collection
from src.algorithms.edit_distance import edit_distance
import random

# Reference to "intents collection"
collection = get_collection("intents")

def get_reply(user_message: str) -> str:
    """
    Give a user message, find a matching intent in MongoDB
    and return one of its responses. If not match is found,
    return a default fallback response
    
    Matching logic:
    1. exact match (fast)
    2. fuxxy match using edit distance with dynamic threshold
    """

    # match by exact intent name. Step 1
    intent = collection.find_one({"intent": user_message.lower()}, {"_id": 0})
    if intent:
        # randomly choose a response from the list
        return random.choice(intent["responses"])
    
    # Fuzzy match: find closest intent
    all_intents = list(collection.find({}, {"_id": 0}))
    if not all_intents:
        return "I don't understand yet."
    
    closest_intent = None
    min_distance = float("inf")

    for candidate in all_intents:
        dist = edit_distance(user_message.lower(), candidate["intent"].lower())
        if dist < min_distance:
            min_distance = dist
            closest_intent = candidate

    # dynamic threshold
    # Short words: at least 2 edits allowed
    # longer words: allow up to 1/3 of word length
    threshold = max(2, len(user_message) // 3)

    if closest_intent and min_distance <= threshold:
        return random.choice(closest_intent["responses"])
    
    return "I don't understand yet"
