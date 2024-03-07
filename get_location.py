import requests
import re


def get_destination(destination_address: str) -> None:
    formatted_address = re.sub(
        r'\s+', '+', destination_address.replace(",", "")).replace(".", "").strip()
    url = f"https://geocode.maps.co/search?q={formatted_address}&api_key=65e8c024164ff880722812epqe3caac"
    response = requests.get(url=url)

    if response.status_code == 200:  # Check if the request was successful
        destination_data = response.json()
        if destination_data:  # Check if the response contains data
            lat = destination_data[0]["lat"]
            lon = destination_data[0]["lon"]
            print(lat, lon)
        else:
            print("No results found for the given address.")
    else:
        print(
            f"Failed to get data from the API, status code: {response.status_code}")


destination_address = input("Enter your destination address: ")
get_destination(destination_address)
