import requests
import os


class NWSForecast:
    def __init__(self):
        self.user_agent = os.getenv("NWS_USER_AGENT")

    def get_gridpoints(self, lat, lon):
        # Get gridpoint info from NWS API
        gridpoint = requests.get(f"https://api.weather.gov/points/{lat},{lon}")
        print(gridpoint.json())
        print(gridpoint.headers)


