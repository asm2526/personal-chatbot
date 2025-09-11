"""
Chatbot service logic
handles message processing and returns appropriate replies
based ons tored intents in MongoDB
"""

from src.core.database import get_collection
from src.algorithms.edit_distance import edit_distance
# from src.algorithms.tfidf import TfidfMatcher
# tfidf is now obsolete due to more robust sentence embedding matcher
from src.algorithms.embedding_matcher import EmbeddingMatcher
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
    
    # Embedding sentence similairty (multi-intent)
    matcher = EmbeddingMatcher(all_intents)
    emb_matches = matcher.match(user_message, top_k = 2)

    if emb_matches:
        print(f"[DEBUG] Embedding matches for '{user_message}':")
        for r in emb_matches:
            print(f"   - {r['intent']} (score={r['score']:.3f})")

        best = emb_matches[0]

        if len(emb_matches) > 1:
            second = emb_matches[1]
            print(
                f"[Debug] Top1={best['intent']} ({best['score']:.3f}), "
                f"Top2={second['intent']} ({second['score']:.3f}), "
                f"Diff={best['score']-second['score']:.3f}"
            )

            # if both are close, combine responses
            if best["score"] - second["score"] < 0.1 and second["score"] > 0.35:
                reply1 = random.choice(best["responses"])
                reply2 = random.choice(second["responses"])
                combined = f"{reply1} {reply2}"
                return combined

        # otherwise return best single intent
        chosen = random.choice(best["responses"])
        print(f"[DEBUG] Best single intent chosen: {best['intent']} -> {chosen}")
        return chosen

    
    print("[DEBUG] No embedding matches found")
    return "I don't understand yet"