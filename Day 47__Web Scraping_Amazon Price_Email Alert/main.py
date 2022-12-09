import smtplib
import requests
from bs4 import BeautifulSoup
import lxml


# ============================ Step 1: Scrape Amazon ============================
URL = "https://www.amazon.com/Apple-AirPods-Charging-Case-Renewed/dp/B07SKLLYTW/ref=sr_1_1?crid=1TNZ91PEOKGGS&keywords=apple+airpods+2+with+charging+case+-+white+renewed&qid=1664725512&qu=eyJxc2MiOiIwLjY1IiwicXNhIjoiMC42OCIsInFzcCI6IjAuODUifQ%3D%3D&sprefix=Apple+AirPods+2+with+Charging+Case+-+White+%28Renewed%29%2Caps%2C748&sr=8-1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,vi;q=0.8"
}
rsp = requests.get(url=URL, headers=headers)
rsp.raise_for_status()
# print(rsp.text)

bs4 = BeautifulSoup(rsp.content, "lxml")
for tag in bs4.find_all(name="span"):
    if tag.get("aria-hidden") == "true":
        print(tag)

# ============================ Step 2: Email Alert ============================
MY_EMAIL = "lamasia30@gmail.com"
MY_PASSWORD = "zwtmosuqijrdvyam"
with smtplib.SMTP("smtp.gmail.com", 587) as conn:
    conn.starttls()
    conn.login(user=MY_EMAIL, password=MY_PASSWORD)
    conn.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Price cheaper alert!"
    )
    