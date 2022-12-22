import requests
from twilio.rest import Client
from datetime import datetime, timedelta
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
OWM_APIKEY = "69f04e4613056b159c2761a9d9e664d2"
# API_Key = "441957c30d0b20c0c4862a84f1c58dc9"
params = {
    "lat": -33.865143,
    "lon": 151.209900,
    "appid": OWM_APIKEY,
    "exclude": "current,minutely,hourly"
}
rsp = requests.get(url=OWM_ENDPOINT, params=params)
rsp.raise_for_status()
data = rsp.json()
lst_data = data["daily"]
lst_weather = []
for hour in lst_data:
    hourly_weather = hour["weather"][0]["main"]
    if hourly_weather not in lst_weather:
        lst_weather.append(hourly_weather)
report_weather = f'\n{",".join(lst_weather)}'
# print(report_weather)

# ================================================================
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
TEQUILA_HEADERS = {
    "apikey": "Rpevg6zmAqawGEDiIhra3R9qGVPquls-",
}
date_from = datetime.strftime(datetime.today() + timedelta(days=1), "%d/%m/%Y")
date_to = datetime.strftime(datetime.today() + timedelta(days=180), "%d/%m/%Y")
_params = {
    "fly_from": "DAD",
    "fly_to": "SYD",
    "date_from": date_from,
    "date_to": date_to,
    "nights_in_dst_from": 60,
    "nights_in_dst_to": 90,
    "curr": "VND",
    "flight_type": "round",
}

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)
rsp = session.get(url=TEQUILA_ENDPOINT, headers=TEQUILA_HEADERS, params=_params)

# rsp = requests.get(url=TEQUILA_ENDPOINT, headers=TEQUILA_HEADERS, params=_params)
rsp.raise_for_status()
data = rsp.json()
# print(len(data["data"]))
lowest_price = min([route["price"] for route in data["data"]])
sms = f'\nLowest price is {round(lowest_price)} VND'
for route in data["data"]:
    if route["price"] == lowest_price:
        sms += f'\n{route["route"][0]["local_departure"].split("T")[0]} - ' \
              f'{route["route"][-1]["local_arrival"].split("T")[0]} ({route["nightsInDest"]} days - ' \
              f'{",".join(route["airlines"])})'
# print(sms)

# ================================================================
TWILIO_SID = "AC2915a8b4dcb2e78be04319ecda8f4446"
TWILIO_TOKEN = "25b2c7b6117f8f125aa43746dda59b10"
FROM = "+18477801958"
TO = "+84977201771"

_body = f"\nWeather forecast (8 days) and cheapest flight (6 months) in Sydney:{report_weather}{sms}\nHave a nice day!"
print(_body)

client = Client(TWILIO_SID, TWILIO_TOKEN)
message = client.messages.create(body=_body, from_=FROM, to=TO)
print(message.status)
