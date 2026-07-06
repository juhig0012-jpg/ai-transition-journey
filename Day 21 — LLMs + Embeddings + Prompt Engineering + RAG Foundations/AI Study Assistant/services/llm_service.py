# ==========================================================
# Import Gemini Client Library
# ==========================================================
from google import genai

# Load environment variables
from dotenv import load_dotenv

# Used to access environment variables
import os

# ==========================================================
# Load .env file
# ==========================================================
load_dotenv()

# ==========================================================
# Read API Key from .env
# ==========================================================
api_key = os.getenv("GEMINI_API_KEY")
print("API Key:", api_key)

# Check whether API Key exists
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# ==========================================================
# Create Gemini Client
# ==========================================================
client = genai.Client(api_key=api_key)

# ==========================================================
# Function to Ask Gemini
# ==========================================================
def ask_llm(question):

    print("Inside ask_llm()")
    print("Question:", question)

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question
        )

        print(response)

        return response.text

    except Exception as e:

        print("Gemini Error:", e)
        return f"Error: {e}"

    try:

        # Send question to Gemini
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question
        )

        # Return generated answer
        return response.text

    except Exception as e:

        # Return error if anything goes wrong
        return f"Error : {str(e)}"