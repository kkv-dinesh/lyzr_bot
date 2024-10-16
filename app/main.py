import os
import weaviate
from fastapi import FastAPI, Form, HTTPException
from pydantic import BaseModel
from lyzr import QABot
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

openai_api_key = os.getenv("OPENAI_API_KEY")

WEAVIATE_URL = os.getenv("WEAVIATE_URL", "http://weaviate:8080")
client = weaviate.Client(WEAVIATE_URL)

pdf_path = "/data/KME_Products.pdf"
my_chatbot = QABot.pdf_qa(input_files=[pdf_path])

class QueryRequest(BaseModel):
    query: str

from fastapi import FastAPI

app = FastAPI()

@app.post("/query")
async def query_pdf(query_request: QueryRequest):
    response = my_chatbot.query(query_request.query)  # Access the query string directly
    return {"query": query_request.query, "response": response}


@app.get("/weaviate-health")
async def weaviate_health_check():
    try:
        is_live = client.is_live()
        return {"Weaviate Live": is_live}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
