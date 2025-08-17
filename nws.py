import requests
import os


class NWSForecast:
    def __init__(self):
        self.user_agent = os.getenv("NWS_USER_AGENT")

    def test(self):
        print(self.user_agent)

