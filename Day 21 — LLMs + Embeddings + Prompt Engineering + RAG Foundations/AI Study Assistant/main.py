# Import FastAPI framework
from fastapi import FastAPI

# Used to validate incoming request data
from pydantic import BaseModel

# Import our LLM function
from services.llm_service import ask_llm

# Used for reading/writing JSON files
import json

# Used for file and folder operations
import os


# Create FastAPI application object
app = FastAPI()


# File path where chat history will be stored
CHAT_FILE = "data/chat_history.json"


# Request model
# This defines what data API expects from user
class QuestionRequest(BaseModel):

    # User question must be string
    question: str


# Function to save question and answer
def save_chat(question, answer):

    # Create data folder if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Empty list for chat history
    history = []

    # Check if history file already exists
    if os.path.exists(CHAT_FILE):

        # Open existing file in read mode
        with open(CHAT_FILE, "r") as file:

            # Load previous chats
            history = json.load(file)

    # Add new conversation
    history.append({
        "question": question,
        "answer": answer
    })

    # Open file in write mode
    with open(CHAT_FILE, "w") as file:

        # Save updated history
        json.dump(
            history,
            file,
            indent=4
        )


# POST API endpoint
@app.post("/ask")

# Function runs when user calls /ask
def ask_question(request: QuestionRequest):

    # Extract question from request
    question = request.question

    # Send question to LLM
    answer = ask_llm(question)

    # Save conversation
    save_chat(question, answer)

    # Return response
    return {
        "question": question,
        "answer": answer
    }