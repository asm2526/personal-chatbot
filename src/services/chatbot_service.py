"""
Chatbot service logic
handles message processing and returns appropriate replies
based ons tored intents in MongoDB
"""

from src.core.database import get_collection
from src.algorithms.edit_distance import edit_distance
from src.algorithms.tfidf import TfidfMatcher
import random
import re

# Reference to "intents collection"
collection = get_collection("intents")

# new: simple text processing
def preprocess(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text.strip()

def get_reply(user_message: str) -> str:
    """
    Match user message against intents using:
    1. Exact match
    2. Edit distance (fuzzy)
    3. TF-IDF similarity (semantic, multi-intent)
    """

    user_message = preprocess(user_message)

    # exact match
    intent = collection.find_one({"intent": user_message}, {"_id": 0})
    if intent:
        return random.choice(intent["responses"])
    
    # Load all intents
    all_intents = list(collection.find({}, {"_id": 0}))
    if not all_intents:
        return "I don't understand yet."
    
    # fuzzy match
    closest_intent = None
    min_distance = float("inf")
    for candidate in all_intents:
        dist = edit_distance(user_message, candidate["intent"].lower())
        if dist < min_distance:
            min_distance = dist
            closest_intent = candidate
    
    threshold = max(2, len(user_message) // 3)
    if closest_intent and min_distance <= threshold:
        return random.choice(closest_intent["responses"])
    
    #tf-idf mult-intent
    matcher = TfidfMatcher(all_intents)
    tfidf_matches = matcher.match(user_message, threshold=0.15)

    if tfidf_matches:
        responses = [random.choice(m["responses"]) for m in tfidf_matches]
        return " ".join(responses)
    
    return "I don't understand yet"