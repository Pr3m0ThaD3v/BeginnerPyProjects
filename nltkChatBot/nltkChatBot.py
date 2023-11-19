import nltk
import requests
from nltk.chat.util import Chat, reflections


# Adding OpenWeatherMap API functionality

def get_weather(city):
    api_key = "2a4b9568a8e0f60a8bde374656b20e4c"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metrics"}

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        temperature = data["main"]["temp"]
        description = ["weather"][0]["description"]
        return f"The weather in {city} is {description} with a temperature of {temperature} degrees Celsius."
    else:
        return f"Sorry, I couldn't' fetch the weather for {city} at the moment. Please try again later."


# Preprocess Data:
# Define a set of patterns and responses for the chatbot
# Create a simple set
# Add a pattern for the weather queries in the pairs list
pairs = [["hi|hello", ["Hi there!", "Hello!"]], ["how are you", ["I'm good, thank you.", "I'm doing well."]],
         ["What is your name?", ["You can call me Chatbot.", "I'm' just a chatbot."]],
         ["What's up?", ["Hi there!", "Hello!", "Chilling.", "Nothing much."]], ["Weather in (.*)", [get_weather]],
         ["weather in (.*)", [get_weather]],

         # Add more patterns and responses as needed

         ]

chatbot = Chat(pairs, reflections)


def chat_with_user():
    print("Hello! I'm your chatbot. You can type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print("Chatbot", response)


# Run the Chatbot:
# Call the chat_with_user function to start the interaction.

if __name__ == "__main__":
    chat_with_user()
