import requests #used for web requests like GET and POST: webhooks

city = "Las Vegas"
api_key = "7236f3a071f2c52e5ac10ba4e982407c" #os.getenv retrieves the value of an environment variable

def get_weather(city: str, api_key: str) -> None: #function doesnt return anything, just prints the weather
    if not api_key:
        print("Error: API key not found.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}" #calls the OpenWeather API with the city and API key
    response = requests.get(url) #makes a GET request to the OpenWeather API
    data = response.json() #receives the response in JSON format

    if response.status_code != 200: #checks if the response status code is not 200. if it is its good
        print(f"Error: {data.get('message')}")
        return

    temp = data["main"]["temp"] #converts the temperature data from JSON to a Python dictionary
    print(f"Current temperature in {city}: {temp}°C") #prints the temperature in the specified city

if __name__ == "__main__": #checks if the script is being run directly or imported as a module
    get_weather(city, api_key)
