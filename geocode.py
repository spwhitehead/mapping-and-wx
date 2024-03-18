from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable
import main

# Initialize Nominatim Geocoder with a specific user agent and a longer timeout
geolocator = Nominatim(user_agent="wx_destination_app_v1",
                       timeout=5)  # Timeout set to 5 seconds


def get_start_address(start_address: str):
    try:
        # Perform geocoding to get latitude and longitude
        start_location = geolocator.geocode(start_address)

        if start_location:
            return start_location.latitude, start_location.longitude
        else:
            print("Start location could not be geocoded")
    except GeocoderUnavailable:
        print("Geocoder service is unavailable. Please try again later.")


def get_destination_address(destination_address: str):
    try:
        # Perform geocoding to get latitude and longitude
        end_location = geolocator.geocode(destination_address)

        if end_location:
            return end_location.latitude, end_location.longitude
        else:
            print("End location could not be geocoded")
    except GeocoderUnavailable:
        print("Geocoder service is unavailable. Please try again later.")
