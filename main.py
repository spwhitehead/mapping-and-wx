import geocode
import weather
import get_directions


# Get locations
def get_locations():
    start_address = input("Enter your starting address or city: ")
    end_address = input("Enter your destination address or city: ")
    return start_address, end_address


def main():
    # Open the file and read the API key
    with open('ors_api_key.txt', 'r') as file:
        # .strip() removes any leading/trailing whitespace
        ors_api_key = file.read().strip()

    start_address, end_address = get_locations()

    start_latitude, start_longitude = geocode.get_start_address(start_address)
    end_latitude, end_longitude = geocode.get_destination_address(end_address)

    travel_hours = get_directions.get_travel_time(
        ors_api_key, (start_latitude, start_longitude), (end_latitude, end_longitude))
    print(f"Estimated Travel Time: {travel_hours} hours")

    arrival_forecast = weather.fetch_and_display_weather_for_arrival(
        end_latitude, end_longitude, travel_hours)

    print(f"Weather upon arrival: {arrival_forecast}")


if __name__ == "__main__":
    main()
