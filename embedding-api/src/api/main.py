from fastapi import FastAPI
from src.business.hello_service import HelloService
from src.business.embedding_service import EmbeddingService
from src.api.models import EmbeddingRequest, EmbeddingResponse

app = FastAPI(title="Embedding API")

@app.get("/hello")
async def hello_world():
    service = HelloService()
    return {"message": service.get_hello_message()}

@app.post("/embedding", response_model=EmbeddingResponse)
async def generate_embedding(request: EmbeddingRequest):
    service = EmbeddingService()
    embedding = service.generate_embedding(request.content)
    return EmbeddingResponse(embedding=embedding) 

