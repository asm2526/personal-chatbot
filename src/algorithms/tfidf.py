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

        # builds training corpus: intent name + responses + examples
        self.corpus = []
        for i in intents:
            text_parts = [i["intent"]]
            text_parts += i.get("responses", [])
            text_parts += i.get("examples", [])
            self.corpus.append(" ".join(text_parts))

        if self.corpus:
            self.tfidf_matrix = self.vectorizer.fit_transform(self.corpus)
        else:
            self.tfidf_matrix=None

    def match(self, message, threshold=0.15):
        """
        given a user message, return a list of matching intents
        with similarity above threshold
        Returns:
            - [] if not matches
            - [intent1, intent2, ...] if multiple intents match
        """
        if not self.intents or self.tfidf_matrix is None:
            return []
        
        # vectorize query
        query_vec = self.vectorizer.transform([message])
        # cosine similarity with all intents
        similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
            # collect all intents above threshold
        matches = []
        for idx, score in enumerate(similarities):
            if score >= threshold:
                matches.append(self.intents[idx])

        return matches
