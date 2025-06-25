from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class FAQRetriever:
    def __init__(self, faq_blocks):  # now getting a list
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.sentences = faq_blocks  # already cleaned and split

        self.embeddings = self.model.encode(self.sentences, convert_to_numpy=True)
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(self.embeddings)

    def query(self, question, top_k=1, threshold=0.15):
        q_emb = self.model.encode([question], convert_to_numpy=True)
        D, I = self.index.search(q_emb, top_k)
        score = 1 - D[0][0]**0.5
        print(f"Matched score: {score}, FAQ index: {I[0][0]}")
        if score < threshold:
            return None, score
        return self.sentences[I[0][0]], score
