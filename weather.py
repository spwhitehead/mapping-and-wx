import requests
import re
import geocode
from datetime import datetime, timedelta

"""
def fetch_and_display_weather(latitude, longitude):
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
"""


def fetch_and_display_weather_for_arrival(latitude, longitude, travel_hours):
    # Calculate the estimated arrival time
    arrival_time = datetime.now() + timedelta(hours=travel_hours)

    # Weather API endpoint for the given coordinates
    url = f"https://api.weather.gov/points/{latitude},{longitude}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve weather data.")
        return

    # Extract the forecast URL from the response
    forecast_url = response.json()["properties"]["forecastHourly"]
    forecast_response = requests.get(forecast_url)
    if forecast_response.status_code != 200:
        print("Failed to retrieve hourly forecast.")
        return

    # Parse the forecast data
    forecast_data = forecast_response.json()
    periods = forecast_data["properties"]["periods"]

    # Find the forecast closest to the estimated arrival time
    closest_forecast = None
    min_time_diff = float('inf')
    for period in periods:
        forecast_time = datetime.strptime(
            period["startTime"], "%Y-%m-%dT%H:%M:%S%z")
        time_diff = abs((forecast_time - arrival_time).total_seconds())
        if time_diff < min_time_diff:
            closest_forecast = period
            min_time_diff = time_diff

    if closest_forecast:
        # Display the relevant forecast information
        print(f"Weather forecast for your estimated arrival time:")
        print(
            f"Temperature: {closest_forecast['temperature']}°{closest_forecast['temperatureUnit']}")
        print(
            f"Wind: {closest_forecast['windSpeed']} from {closest_forecast['windDirection']}")
        print(f"Forecast: {closest_forecast['shortForecast']}")
    else:
        print("No suitable forecast found for the estimated arrival time.")
