from sentence_transformers import SentenceTransformer
from typing import List

class EmbeddingService:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def generate_embedding(self, content: str) -> List[float]:
        embedding = self.model.encode(content)
        return embedding.tolist() 