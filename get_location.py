import requests
import re


def get_destination(destination_address: str) -> str:
    destination_address = str(input("Enter your destination address: "))
    formatted_address = re.sub(
        r'\s+', '+', destination_address.replace(",", "")).strip()
    return formatted_address


get_destination()

url = f"https://geocode.maps.co/search?q={formatted_address}&api_key=65e8c024164ff880722812epqe3caac"

response = requests.get(url=url)
destination_data = response.json()
