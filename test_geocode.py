from geopy.geocoders import Nominatim

# Initialize Nominatim Geocoder
geolocator = Nominatim(user_agent="geoapiExercises")

# Replace this with the address you want to geocode
address = input(" Enter your destination address: ")

# Perform geocoding to get latitude and longitude
location = geolocator.geocode(address)

if location:
    print(f"Latitude, Longitude: {location.latitude}, {location.longitude}")
else:
    print("Location could not be geocoded")
