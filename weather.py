import requests
import os
from datetime import datetime

api = os.environ["current_weather_data"]  # create your own api first from openweathewrmap
location = input("Enter the city name: ")
link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api # taking location from, user and creating a relevent link
api_link = requests.get(link)
data = api_link.json() # fetching data from the link

temp_city = ((data['main']['temp']) - 273.15)
weather_desc = data['weather'][0]['description']
hmdt = data['main']['humidity']
wind_spd = data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y {} %I:%M:%S %p")

print("-------------------------------------------------------------")
print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print("-------------------------------------------------------------")

print("Current temperature is : {:.2f} ºC".format(temp_city))
print("Current weather desc   :", weather_desc)
print("Current Humidity       :", hmdt, '%')
print("Current wind speed     :", wind_spd, 'kmph')