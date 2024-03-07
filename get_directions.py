import openrouteservice
from openrouteservice.directions import directions

# Replace 'your_api_key_here' with your actual ORS API key
client = openrouteservice.Client(key='your_api_key_here')

# Define the start and end coordinates
# Coordinates are in the format [longitude, latitude]
start_coord = (8.681495, 49.41461)  # Example: Heidelberg, Germany
# Example: Destination in Heidelberg, Germany
end_coord = (8.687872, 49.420318)

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
