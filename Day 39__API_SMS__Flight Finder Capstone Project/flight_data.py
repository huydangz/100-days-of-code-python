from datetime import datetime, timedelta
import requests

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
TEQUILA_HEADERS = {
    "apikey": "Rpevg6zmAqawGEDiIhra3R9qGVPquls-"
}


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.lowest_price = 0
        self.cityFrom = ""
        self.flyFrom = ""
        self.cityTo = ""
        self.flyTo = ""
        self.local_departure = ""
        self.local_arrival = ""

    def get_lowest_price(self, fly_from, fly_to):
        date_from = datetime.strftime(datetime.today() + timedelta(days=1), "%d/%m/%Y")
        date_to = datetime.strftime(datetime.today() + timedelta(days=30), "%d/%m/%Y")
        _params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "curr": "GBP",
            "flight_type": "round",
        }
        rsp = requests.get(url=TEQUILA_ENDPOINT, headers=TEQUILA_HEADERS, params=_params)
        rsp.raise_for_status()
        data = rsp.json()
        self.lowest_price = min([route["price"] for route in data["data"]])
        for route in data["data"]:
            if route["price"] == self.lowest_price:
                self.cityFrom = route["cityFrom"]
                self.flyFrom = route["flyFrom"]
                self.cityTo = route["cityTo"]
                self.flyTo = route["flyTo"]
                self.local_departure = route["route"][0]["local_departure"].split("T")[0]
                self.local_arrival = route["route"][-1]["local_arrival"].split("T")[0]
