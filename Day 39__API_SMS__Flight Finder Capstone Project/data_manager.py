import requests

SHEETY_ENDPOINT = "https://api.sheety.co/6140a437a22f36c13aa11e14794ae510/flightDeals/prices"
SHEETY_HEADERS = {
    "Authorization": "Bearer token_sheety"
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.city_data = []

    def get_city_data(self):
        rsp = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
        rsp.raise_for_status()
        data = rsp.json()
        self.city_data = data["prices"]

    def update_iata_code(self):
        for city in self.city_data:
            _json = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            rsp = requests.put(url=f'{SHEETY_ENDPOINT}/{city["id"]}', headers=SHEETY_HEADERS, json=_json)
            rsp.raise_for_status()
