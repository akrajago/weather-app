import requests
import sys


def display_welcome_message():
    print("Please provide the following information (press enter to skip):")


def get_address():
    fields = ["Building number and street name", "City", "State", "ZIP Code"]
    data = []

    for field in fields:
        val = input(f"{field}: ")
        data.append(val)

    return data


def get_coordinates(address):
    # Match API specification of "%20" in place of spaces
    formatted = [a.replace(" ", "%20") for a in address]
    # Get geolocation info from census.gov API
    geo = requests.get(f"https://geocoding.geo.census.gov/geocoder/locations/"
                       f"address?street={formatted[0]}&city={formatted[1]}"
                       f"&state={formatted[2]}&zip={formatted[3]}"
                       f"&benchmark=Public_AR_Current&format=json")

    matches = geo.json()["result"]["addressMatches"]

    if not matches:
        print(f"Unable to find address: {', '.join(address)}")
        return None, None
    elif len(matches) > 1:
        print("Multiple address matches found")

    return matches[0]["coordinates"]["x"], matches[0]["coordinates"]["y"]


if __name__ == "__main__":
    display_welcome_message()
    location_info = get_address()
    lat, lon = get_coordinates(location_info)

    if not lat:
        sys.exit(1)

    print(lat, lon)
    