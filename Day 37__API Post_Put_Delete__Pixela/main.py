import datetime
import requests

USERNAME = "huydang"
TOKEN = "token_pixela"
ENDPOINT = "https://pixe.la/v1/users"
GRAPH = "graph1"

# ==================== POST ============================
# _json = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# rsp = requests.post(url=ENDPOINT, json=_json)
# rsp.raise_for_status()
# print(rsp.text)

# ===================== POST ===========================
# _url = f"{ENDPOINT}/{USERNAME}/graphs"
# _headers = {
#     "X-USER-TOKEN": TOKEN
# }
# _json = {
#     "id": GRAPH,
#     "name": "Coding Graph",
#     "unit": "lesson",
#     "type": "int",
#     "color": "sora"
# }
# rsp = requests.post(url=_url, headers=_headers, json=_json)
# rsp.raise_for_status()
# print(rsp.text)
# Browse https://pixe.la/v1/users/huydang/graphs/graph1.html

# ===================== POST ===========================
# _url = f"{ENDPOINT}/{USERNAME}/graphs/{GRAPH}"
# _headers = {
#     "X-USER-TOKEN": TOKEN
# }
# _json = {
#     "date": datetime.datetime.today().strftime("%Y%m%d"),
#     "quantity": "4",
# }
# rsp = requests.post(url=_url, headers=_headers, json=_json)
# rsp.raise_for_status()
# print(rsp.text)

# ===================== PUT ===========================
# _url = f'{ENDPOINT}/{USERNAME}/graphs/{GRAPH}/{datetime.datetime.today().strftime("%Y%m%d")}'
# _headers = {
#     "X-USER-TOKEN": TOKEN
# }
# _json = {
#     "quantity": "14",
# }
# rsp = requests.put(url=_url, headers=_headers, json=_json)
# rsp.raise_for_status()
# print(rsp.text)

# ===================== DELETE ===========================
_url = f'{ENDPOINT}/{USERNAME}/graphs/{GRAPH}/20220922'
_headers = {
    "X-USER-TOKEN": TOKEN
}
rsp = requests.delete(url=_url, headers=_headers)
rsp.raise_for_status()
print(rsp.text)