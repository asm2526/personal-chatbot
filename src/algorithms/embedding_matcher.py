"""
Embedding-based similarity matcher for chatbot intents.
Uses sentence-transformers to find semantically similar intents.
"""

from sentence_transformers import SentenceTransformer, util

class EmbeddingMatcher:
    def __init__(self, intents):
        """
        intents: list of dicts with 'intent', 'responses', and optional 'examples'
        """

        self.intents = intents
        self.model = SentenceTransformer("all-MiniLM-L6-v2") # small, fast
        self.intents_texts = []

        for i in intents:
            # build text using intent + examples
            parts = [i["intent"]]
            parts += i.get("examples", [])
            self.intent_texts.append(" ".join(parts))

        if self.intent_texts:
            self.intent_embeddings = self.model.encode(self.intent_texts, convert_to_tensor=True)
        else:
            self.intent_embeddings = None
        
    def match(self, message, threshold=0.4, top_k=2):
        """
        Return top-k intents above a similarity threshold
        """
        if not self.intents or self.intent_embeddings is None:
            return []
        
        query_emb = self.model.encode(message, convert_to_tensor=True)
        cosine_scores = util.cos_sim(query_emb, self.intent_embeddings).cpu().numpy().flatten()

        # rank by similarity
        rank = sorted(
            [(idx, score) for idx, score in enumreate(cosine_scores)],
            key=lambda x: x[1],
            reverse=True
        )

        matches = []
        for idx, score in ranked[:top_k]:
            if score >= threshold:
                matches.append(self.intents[idx])

        return matches
