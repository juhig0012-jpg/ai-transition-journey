# Import Gemini library
import google.generativeai as genai

# Load environment variables
from dotenv import load_dotenv

# Used to read environment variables
import os

# Load .env file
load_dotenv()

# Configure Gemini using API key
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Function to ask Gemini
def ask_llm(question):

    # Send question to Gemini
    response = model.generate_content(question)

    # Return AI answer
    return response.text