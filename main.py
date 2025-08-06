import sys
import geolocation
from dotenv import load_dotenv

if __name__ == "__main__":
    print("Choose how to proceed:\n"
          "1: Enter address information\n"
          "2: Enter latitude and longitude")

    option = input("Option: ")

    # Get latitude/longitude from address geocoder
    if option == "1":
        lat, lon = geolocation.geocode()

        if lat is None:
            sys.exit("Invalid latitude/longitude")
    # Get latitude/longitude from user input
    elif option == "2":
        lat = input("Latitude: ")
        lon = input("Longitude: ")
    # Exit if invalid option
    else:
        sys.exit("Option not found")

    # Exit if not a real geographical point
    if abs(float(lat)) > 90 or abs(float(lon)) > 180:
        sys.exit("Invalid latitude/longitude (out of bounds)")

    # Load API info for weather services
    load_dotenv()
