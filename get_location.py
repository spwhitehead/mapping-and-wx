import requests
import re

with open('geocode_api_key.txt', 'r') as file:
    api_key = file.read().strip()  # .strip() removes any leading/trailing whitespace


def get_destination(destination_address: str) -> None:
    end_formatted_address = re.sub(
        r'\s+', '+', destination_address.replace(",", "")).replace(".", "").strip()
    url = f"https://geocode.maps.co/search?q={end_formatted_address}&api_key={api_key}"
    response = requests.get(url=url)

    if response.status_code == 200:  # Check if the request was successful
        destination_data = response.json()
        if destination_data:  # Check if the response contains data
            lat_end = destination_data[0]["lat"]
            lon_end = destination_data[0]["lon"]
            return (lat_end, lon_end)
        else:
            print("No results found for the destination address.")
    else:
        print(
            f"Failed to get destination data from the server, status code: {response.status_code}")


def get_start_address(start_address: str) -> None:
    start_formatted_address = re.sub(
        r'\s+', '+', start_address.replace(",", "")).replace(".", "").strip()
    url = f"https://geocode.maps.co/search?q={start_formatted_address}&api_key={api_key}"
    response = requests.get(url=url)

    if response.status_code == 200:  # Check if the request was successful
        start_data = response.json()
        if start_data:  # Check if the response contains data
            lat_start = start_data[0]["lat"]
            lon_start = start_data[0]["lon"]
            return (lat_start, lon_start)
        else:
            print("No results found for the starting address.")
    else:
        print(
            f"Failed to get starting data from the server, status code: {response.status_code}")


if __name__ == "__main__":
    start_address = input("Enter your starting address: ")
    destination_address = input("Enter your destination address: ")
    get_start_address(start_address)
    get_destination(destination_address)
