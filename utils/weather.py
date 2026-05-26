import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

print("Loaded API KEY:", API_KEY)   # Debug


def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    print("Request URL:", url)   # Debug

    response = requests.get(url)

    print("Status Code:", response.status_code)  # Debug
    print("Response:", response.text)            # Debug

    if response.status_code != 200:
        return None

    return response.json()