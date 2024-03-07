import openrouteservice
from openrouteservice.directions import directions
import map_with_wx

# Open the file and read the API key
with open('ors_api_key.txt', 'r') as file:
    api_key = file.read().strip()  # .strip() removes any leading/trailing whitespace

# Initialize the ORS client with the API key read from file
client = openrouteservice.Client(key=api_key)

# Define the start and end coordinates

start_coord = (8.681495, 49.41461)
end_coord = (map_with_wx.latitude, map_with_wx.longitude)

# Request directions via driving
routes = directions(client, start_coord, end_coord)

# Extract travel time from the routes dictionary
# The duration is given in seconds
duration_seconds = routes['routes'][0]['summary']['duration']

# Convert duration to minutes and hours for better readability
duration_minutes = duration_seconds / 60
duration_hours = duration_minutes / 60

print(f"Travel Time: {duration_seconds} seconds")
print(f"Travel Time: {duration_minutes} minutes")
print(f"Travel Time: {duration_hours} hours")
