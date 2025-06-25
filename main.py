import geolocation

if __name__ == "__main__":
    lat, lon = geolocation.geocode()

    if lat:
        print(lat, lon)

    # TODO: option to enter lat/lon manually?
