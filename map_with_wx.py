import requests
import re
import get_location

destination_address = input("Enter your destination address: ")
location_data = get_location.get_destination(destination_address)

latitude = location_data[0]
longitude = location_data[1]

url = f"https://api.weather.gov/points/{latitude},{longitude}"

response = requests.get(url=url)
weather_data = response.json()
# print(weather_data)

forecast_city = weather_data["properties"]["relativeLocation"]["properties"]["city"]
forecast_state = weather_data["properties"]["relativeLocation"]["properties"]["state"]
forecast_url = weather_data["properties"]["forecastHourly"]
response = requests.get(url=forecast_url)
forecast = response.json()
print()

periods = forecast["properties"]["periods"]
current_period = periods[0]

current_temperature = current_period["temperature"]
current_wind_speed = current_period["windSpeed"]
current_wind_direction = current_period["windDirection"]
weather_condition = current_period["shortForecast"]
is_daytime = current_period["isDaytime"]
print()
print(f"Current weather in {forecast_city}, {forecast_state}")
print()
print(f"Current Temperature: \t\t{current_temperature}")
print(f"Winds are coming from the: \t{current_wind_direction}")
print(f"Winds are at: \t\t\t{current_wind_speed}")
print(f"The weather is currently: \t{weather_condition}")


def is_sunny(weather_condition):
    if is_daytime and re.search(r"sunny", weather_condition, re.IGNORECASE):
        print("Take your sunglasses")
    else:
        print("No sunglasses needed outside right now.")


is_sunny(weather_condition)
