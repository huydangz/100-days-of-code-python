import datetime
import requests
import os
from twilio.rest import Client

STOCK = "TSLA"

# ========================== Step 1 - get close price of 2 days before ================
_url_stock = "https://www.alphavantage.co/query"
_apikey_stock = "OX6Y5QN54VTR9CII"
_params_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": _apikey_stock
}
rsp = requests.get(url=_url_stock, params=_params_stock)
rsp.raise_for_status()
data = rsp.json()

# key1 = str(datetime.datetime.today() - datetime.timedelta(1)).split(" ")[0]
# key2 = str(datetime.datetime.today() - datetime.timedelta(2)).split(" ")[0]
# data1 = float(data["Time Series (Daily)"][key1]["4. close"])
# data2 = float(data["Time Series (Daily)"][key2]["4. close"])
lst_stock = [value for (key, value) in data["Time Series (Daily)"].items()]
data1 = float(lst_stock[0]["4. close"])
data2 = float(lst_stock[1]["4. close"])
delta = abs((data1 - data2) / data1 * 100)

print(delta)

# ============================= Step 2 - get 3 popular news related company =================
_url_news = "https://newsapi.org/v2/everything"
_apikey_news = "f718c38a601c4e3f8c3d577e07ffdc99"
_params_news = {
    "q": "tesla",
    "searchIn": "title",
    "sortBy": "popularity",
    "apiKey": _apikey_news
}
rsp = requests.get(url=_url_news, params=_params_news)
rsp.raise_for_status()
data = rsp.json()
lst_articles = [data["articles"][n] for n in range(0, 3)]

for article in lst_articles:
    print(article["title"])

# ============================ Step 3 - send SMS with price change and news ===================
# account_sid = "AC2915a8b4dcb2e78be04319ecda8f4446"
# auth_token = "2eda7e0387d9f22d78c48ed024d920b4"
account_sid = os.environ["ENV_ACCOUNT_SID"]
auth_token = os.environ["ENV_AUTH_TOKEN"]
trend = "🔺"
if data1 < data2:
    trend = "🔻"
_title = f"{STOCK}: {trend}{round(delta)}%"
_from = "+13025644808"
_to = "+84977201771"

client = Client(account_sid, auth_token)
for article in lst_articles:
    _body = f'{_title}\nHeadline: {article["title"]}\nBrief: {article["description"]}'
    message = client.messages.create(body=_body, from_=_from, to=_to)
    print(message.status)
