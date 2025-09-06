import sys
import geolocation
import nws
from dotenv import load_dotenv

if __name__ == "__main__":
    print("Choose how to proceed (US locations only):\n"
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

        # Exit if not a real geographical point
        if abs(float(lat)) > 90 or abs(float(lon)) > 180:
            sys.exit("Invalid latitude/longitude (out of bounds)")
        elif not geolocation.check_coordinates(lat, lon):
            sys.exit("Latitude/longitude not in US")
    # Exit if invalid option
    else:
        sys.exit("Option not found")

    # Load API info for weather services
    load_dotenv()

    nws_weather = nws.NWSForecast()
    # nws_weather.get_gridpoints(lat, lon)
