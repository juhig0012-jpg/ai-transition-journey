from utils.weather import get_weather

city = input("Enter city name: ")

weather_data = get_weather(city)

if weather_data:
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    condition = weather_data["weather"][0]["description"]

    print("\nWeather Details")
    print("-------------------")
    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition}")

else:
    print("City not found or API error.")