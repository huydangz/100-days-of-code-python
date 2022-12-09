import requests

SHEETY_ENDPOINT = "https://api.sheety.co/6140a437a22f36c13aa11e14794ae510/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/6140a437a22f36c13aa11e14794ae510/flightDeals/users"
SHEETY_HEADERS = {
    "Authorization": "Bearer token_sheety"
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.city_data = []
        self.user_data = []

    def get_city_data(self):
        rsp = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
        rsp.raise_for_status()
        data = rsp.json()
        self.city_data = data["prices"]

    def get_user_data(self):
        rsp = requests.get(url=SHEETY_USERS_ENDPOINT, headers=SHEETY_HEADERS)
        rsp.raise_for_status()
        data = rsp.json()
        self.user_data = data["users"]

    def update_iata_code(self):
        for city in self.city_data:
            _json = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            rsp = requests.put(url=f'{SHEETY_ENDPOINT}/{city["id"]}', headers=SHEETY_HEADERS, json=_json)
            rsp.raise_for_status()

    def user_input(self):
        print("Welcome to Hugh's Flight Club")
        print("We find the best flight deals and email you")
        first_name = input("What is your first name?\n")
        last_name = input("What is your last name?\n")
        email1 = input("What is your email?\n")
        email2 = input("Type your email again:\n")
        if email1 == email2:
            print("You're in the club!")
            _json = {
                "user": {
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": email1
                }
            }
            rsp = requests.post(url=SHEETY_USERS_ENDPOINT, headers=SHEETY_HEADERS, json=_json)
            rsp.raise_for_status()
        else:
            print("Your emails not match")
