# A weather app that fetches weather data

# Make it work!
# Weather API Site: https://home.openweathermap.org

import requests


def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Construct the API URL with the provided parameters
    params = {"q": city, "appid": api_key, "units": "imperial"}
    headers = {"Authorization" f"Bearer {api_key}"}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: Unable to fetch weather data. Status Code: {response.status_code}")
        return None


def display_weather(weather_data):
    if weather_data:
        # Extract relevant information from the API response
        city = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature} °F")
        print(f"Description: {description}")
    else:
        print("No weather data to display.")


# Replace 'YOUR_API_KEY', 'LATITUDE', and 'LONGITUDE' with your actual Open-Meteo API key and coordinates

api_key = "Enter your own API Key"
city = input("Enter the city name:")

# Fetch and display weather data

weather_data = get_weather(api_key, city)
display_weather(weather_data)


