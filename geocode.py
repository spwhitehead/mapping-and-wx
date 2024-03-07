from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable

# Initialize Nominatim Geocoder with a specific user agent and a longer timeout
geolocator = Nominatim(user_agent="wx_destination_app_v1",
                       timeout=5)  # Timeout set to 5 seconds


def get_start_address(start_address: str):
    try:
        # Perform geocoding to get latitude and longitude
        location = geolocator.geocode(start_address)

        if location:
            return location.latitude, location.longitude
        else:
            print("Location could not be geocoded")
    except GeocoderUnavailable:
        print("Geocoder service is unavailable. Please try again later.")


def get_destination_address(destination_address: str):
    try:
        # Perform geocoding to get latitude and longitude
        location = geolocator.geocode(destination_address)

        if location:
            return location.latitude, location.longitude
        else:
            print("Location could not be geocoded")
    except GeocoderUnavailable:
        print("Geocoder service is unavailable. Please try again later.")


if __name__ == "__main__":
    start_address = input("Enter your starting address or city: ")
    destination_address = input("Enter your destination address or city: ")
    get_start_address(start_address)
    get_destination_address(destination_address)
