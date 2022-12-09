import datetime
import smtplib
import time
import requests

MY_LAT = -35.4707
MY_LONG = -52.2667
MY_EMAIL = "lamasia30@gmail.com"
MY_PASSWORD = "zwtmosuqijrdvyam"

def is_overhead():
    rsp = requests.get(url="http://api.open-notify.org/iss-now.json")
    rsp.raise_for_status()
    data = rsp.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])
    return -5 <= iss_lat - MY_LAT <= 5 and -5 <= iss_long - MY_LONG <= 5

def is_darktime():
    params = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    rsp = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
    rsp.raise_for_status()
    data = rsp.json()
    hour_sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    hour_sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    hour_now = datetime.datetime.now().hour

    return (hour_now - hour_sunset) * (hour_now - hour_sunrise) <= 0

def send_email_for_lookup():
    with smtplib.SMTP("smtp.gmail.com", 587) as conn:
        conn.starttls()
        conn.login(user=MY_EMAIL, password=MY_PASSWORD)
        conn.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"subject:Lookup ISS Overhead\n\nISS now is overhead your area. Just look up it !"
        )
def check_iss():
    if is_overhead() and is_darktime():
        send_email_for_lookup()

while True:
    check_iss()
    time.sleep(60)

# =============================================================================
# # import datetime
#
# import requests
#
# params = {
#     "lat": 16.054407,
#     "lng": 108.202164,
#     "formatted": 0
# }
# rsp = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
# rsp.raise_for_status()
# data = rsp.json()
# print(data)
#
# print(datetime.datetime.now())

# =============================================================================
# from tkinter import *
# import requests
#
#
# def get_quote():
#     rsp = requests.get(url="https://api.kanye.rest")
#     rsp.raise_for_status()
#     data = rsp.json()
#     quote = data["quote"]
#     canvas.itemconfig(quote_text, text=quote)
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
#
#
# window.mainloop()