# ==========================================================
# Import FastAPI
# ==========================================================
from fastapi import FastAPI

# Used to validate request body
from pydantic import BaseModel

# Import Gemini Function
from services.llm_service import ask_llm

# Used for JSON operations
import json

# Used for file handling
import os

# ==========================================================
# Create FastAPI App
# ==========================================================
app = FastAPI(
    title="AI Study Assistant",
    description="Powered by Google Gemini",
    version="1.0"
)

# ==========================================================
# Chat History File
# ==========================================================
CHAT_FILE = "data/chat_history.json"

# ==========================================================
# Request Model
# ==========================================================
class QuestionRequest(BaseModel):

    # User question
    question: str

# ==========================================================
# Save Chat History
# ==========================================================
def save_chat(question, answer):

    # Create data folder if missing
    os.makedirs("data", exist_ok=True)

    history = []

    # Read previous history
    if os.path.exists(CHAT_FILE):

        with open(CHAT_FILE, "r", encoding="utf-8") as file:

            try:
                history = json.load(file)

            except json.JSONDecodeError:
                history = []

    # Add latest conversation
    history.append({

        "question": question,
        "answer": answer

    })

    # Save file
    with open(CHAT_FILE, "w", encoding="utf-8") as file:

        json.dump(

            history,
            file,
            indent=4,
            ensure_ascii=False

        )

# ==========================================================
# Home Route
# ==========================================================
@app.get("/")
def home():

    return {

        "message": "AI Study Assistant is Running Successfully."

    }

# ==========================================================
# Ask AI
# ==========================================================
@app.post("/ask")
def ask_question(request: QuestionRequest):

    # Get user question
    question = request.question

    # Ask Gemini
    answer = ask_llm(question)

    # Save conversation
    save_chat(question, answer)

    # Return response
    return {

        "question": question,
        "answer": answer

    }