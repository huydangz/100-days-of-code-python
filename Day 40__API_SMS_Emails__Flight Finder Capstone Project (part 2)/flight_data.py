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
        self.stop_overs = 0
        self.via_city = []
        self.local_departure = ""
        self.local_arrival = ""

    def get_lowest_price(self, fly_from, fly_to):
        date_from = datetime.strftime(datetime.today() + timedelta(days=1), "%d/%m/%Y")
        date_to = datetime.strftime(datetime.today() + timedelta(days=100), "%d/%m/%Y")
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
        try:
            rsp.raise_for_status()
            data = rsp.json()["data"][0]
        except:
            pass
        else:
            self.lowest_price = data["price"]
            self.cityFrom = data["cityFrom"]
            self.flyFrom = data["flyFrom"]
            self.cityTo = data["cityTo"]
            self.flyTo = data["flyTo"]

            self.via_city = []
            for route in data["route"]:
                if route["cityTo"] not in self.via_city and route["cityTo"] != self.cityFrom and route["cityTo"] != self.cityTo:
                    self.via_city.append(route["cityTo"])
            self.stop_overs = len(self.via_city)

            self.local_departure = data["route"][0]["local_departure"].split("T")[0]
            self.local_arrival = data["route"][-1]["local_arrival"].split("T")[0]
