import openrouteservice
from openrouteservice.directions import directions


def get_travel_time(api_key, start_coord, end_coord):
    # Initialize the ORS client with the API key read from file
    client = openrouteservice.Client(key=api_key)

    routes = directions(client, [start_coord, end_coord])
    duration_seconds = routes['routes'][0]['summary']['duration']
    duration_hours = duration_seconds / 3600

    return duration_hours
