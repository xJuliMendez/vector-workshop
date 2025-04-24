from pydantic import BaseModel
from typing import List

class EmbeddingRequest(BaseModel):
    content: str

class EmbeddingResponse(BaseModel):
    embedding: List[float] 