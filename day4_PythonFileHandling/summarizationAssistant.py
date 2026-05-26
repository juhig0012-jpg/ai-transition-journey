import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted

# Configure API Key
genai.configure(api_key="AIzaSyCS6Uap4cCgD8qdzS4NSaBybku8c9r7yFA")

# Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")


def summarize_text(text):
    prompt = f"Summarize the following:\n{text}"

    try:
        response = model.generate_content(prompt)
        return response.text

    except ResourceExhausted:
        return "API quota exceeded. Please wait and try again later."


if __name__ == "__main__":

    print("=== AI Summarization Assistant ===")

    user_input = input("\nEnter text to summarize:\n")

    summary = summarize_text(user_input)

    print("\n=== Summary ===")
    print(summary)