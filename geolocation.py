import requests


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
    # Assemble params for API call
    fields = ["street", "city", "state", "zip"]
    payload = dict(zip(fields, address)) | {"benchmark": "Public_AR_Current",
                                            "format": "json"}

    # Get geolocation info from census.gov API
    geo = requests.get(f"https://geocoding.geo.census.gov/"
                       f"geocoder/locations/address", params=payload).json()

    # Print any errors returned by geocoding API
    if "errors" in geo:
        print("ERROR: Bad input data")
        for error in geo["errors"]:
            print("-", error)
        return None, None

    matches = geo["result"]["addressMatches"]

    if not matches:
        print(f"Unable to find address: {', '.join(address)}")
        return None, None
    elif len(matches) > 1:
        print("Multiple address matches found. Please select the number "
              "which corresponds to your address:")
        # List out each match
        for index, address_match in enumerate(matches):
            print(f"{index + 1}: {address_match['matchedAddress']}")

        selected = input("Matched address: ")
        # Return info of selected match
        if (i := int(selected)) <= len(matches):
            return matches[i - 1]["coordinates"]["y"], matches[i - 1]["coordinates"]["x"]
        else:
            print("Unable to find match")
            return None, None
    else:
        # Return info of first/only match
        return matches[0]["coordinates"]["y"], matches[0]["coordinates"]["x"]


def geocode():
    display_welcome_message()
    location_info = get_address()
    return get_coordinates(location_info)


def check_coordinates(lat, lon):
    # Assemble params for API call
    payload = {"x": lon, "y": lat, "benchmark": "Public_AR_Current",
               "vintage": "Current_Current", "format": "json"}

    # Get geolocation info from census.gov API
    geo = requests.get(f"https://geocoding.geo.census.gov/"
                       f"geocoder/geographies/coordinates", params=payload).json()

