"""
TF-IDF similarity algorithm for chatbot intents.
Uses scikit-learn to vectorize text and find the closest intent
based on cosine similarity.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class TfidfMatcher:
    def __init__(self, intents):
        """
        intents: list of dicts
        """
        self.intents = intents
        self.vectorizer = TfidfVectorizer()
        # Build corpus from intent names + responses
        self.intent_names = [i["intent"] for i in intents]
        self.corpus = [i["intent"] + " " + " ".join(i.get("responses", [])) for i in intents]
        self.tfidf_matrix = self.vectorizer.fit_transform(self.corpus)
    
    def match(self, message, threshold=0.1):
        """
        Given a user message, return the closest matching intent
        if similarity is above threshold, else None.
        """
        if not self.intents:
            return None
        
        query_vec = self.vectorizer.transform([message])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()

        best_idx = np.argmax(similarities)
        best_score = similarities[best_idx]

        if best_score >= threshold:
            return self.intents[best_idx]
        return None