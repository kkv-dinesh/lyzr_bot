import os
from fastapi import FastAPI
from lyzr import QABot
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Path to the PDF file
pdf_path = "data/KME_Products.pdf"

# Initialize the QABot with the PDF
my_chatbot = QABot.pdf_qa(input_files=[pdf_path])

@app.post("/query")
async def query_pdf(query: str):
    response = my_chatbot.query(query)
    return {"query": query, "response": response}
