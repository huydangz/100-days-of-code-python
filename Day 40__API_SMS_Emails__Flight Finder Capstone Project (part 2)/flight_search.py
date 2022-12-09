import requests

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_HEADERS = {
    "apikey": "Rpevg6zmAqawGEDiIhra3R9qGVPquls-"
}


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_iata_code(self, city):
        _params = {
            "term": city,
            "location_types": "city"
        }
        rsp = requests.get(url=TEQUILA_ENDPOINT, headers=TEQUILA_HEADERS, params=_params)
        rsp.raise_for_status()
        data = rsp.json()
        return data["locations"][0]["code"]
