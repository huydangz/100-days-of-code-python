import datetime
import requests
import os

# ======================== Step 1 API query to exercise/duration/calories ================
_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
_headers = {
    "x-app-id": os.environ["APP_ID"],
    "x-app-key": os.environ["API_KEY"]
}
_json = {
    "query": input("Tell me which exercises you did today: "),
    "gender": "male",
    "weight_kg": 60,
    "height_cm": 160,
    "age": 38
}
rsp = requests.post(url=_url, headers=_headers, json=_json)
rsp.raise_for_status()
data = rsp.json()
print(data)

# ========================= Step 2 API post exercise to google sheet ===============

# _url = "https://api.sheety.co/4df454cc3eabff8e5dce872757f000b9/workoutTracking/workouts"
# rsp = requests.get(url=_url)
# data = rsp.json()
# rsp.raise_for_status()
# print(rsp.text)
# print(data)

_url = "https://api.sheety.co/4df454cc3eabff8e5dce872757f000b9/workoutTracking/workouts"
_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
}
for exercise in data["exercises"]:
    _json = {
        "workout": {
            "date": datetime.datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    rsp = requests.post(url=_url, headers=_headers, json=_json)
    rsp.raise_for_status()
    print(rsp.text)