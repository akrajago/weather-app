import sys
import geolocation

if __name__ == "__main__":
    print("Choose how to proceed:\n"
          "1: Enter address information\n"
          "2: Enter latitude and longitude")

    option = input("Option: ")

    if option == "1":
        lat, lon = geolocation.geocode()

        if lat is not None:
            sys.exit("Invalid latitude/longitude")
    elif option == "2":
        lat = input("Latitude: ")
        lon = input("Longitude: ")
    else:
        sys.exit("Option not found")
