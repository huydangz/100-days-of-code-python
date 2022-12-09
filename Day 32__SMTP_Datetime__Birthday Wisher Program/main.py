import datetime
import random
import smtplib
import pandas
import pathlib

MY_EMAIL = "lamasia30@gmail.com"
MY_PASSWORD = "zwtmosuqijrdvyam"
PLACE_HOLDER = "[NAME]"

script_path = pathlib.Path(__file__).parent.resolve()
# current_path = pathlib.Path().resolve()
# print(script_path)
# print(current_path)

data = pandas.read_csv(f"{script_path}/birthdays.csv")
dict_data = data.to_dict(orient="records")

day = datetime.datetime.now().day
month = datetime.datetime.now().month

def compose_for(name):
    with open(f"{script_path}/letter_templates/letter_{random.randint(1, 3)}.txt", mode="r") as f:
        return f.read().replace(PLACE_HOLDER, name)

for person in dict_data:
    if person["day"] == day and person["month"] == month:
        name = person["name"]
        with smtplib.SMTP("smtp.gmail.com", 587) as conn:
            conn.starttls()
            conn.login(user=MY_EMAIL, password=MY_PASSWORD)
            conn.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person["email"],
                msg=f"subject:Happy Birthday\n\n{compose_for(name)}"
            )

# ===============================================================
# import random
# import smtplib
# import datetime
#
#
# def today_is_wednesday():
#     return datetime.datetime.now().weekday() == 2
#
#
# def random_quote():
#     with open("quotes.txt", mode="r") as f:
#         list_quotes = f.readlines()
#         list_quotes = [quote.strip() for quote in list_quotes]
#         return random.choice(list_quotes)
#
#
# if today_is_wednesday():
#     user = "lamasia30"
#     password = "zwtmosuqijrdvyam"
#     src_mail = "lamasia30@gmail.com"
#     dest_mail = "lamasia30@gmail.com"
#
#     with smtplib.SMTP("smtp.gmail.com", 587) as conn:
#         conn.starttls()
#         conn.login(user=user, password=password)
#         conn.sendmail(
#             from_addr=src_mail,
#             to_addrs=dest_mail,
#             msg=f"subject:Quote for today\n\nHi,\nHave a nice day\n{random_quote()}\n\nBrgs."
#         )
#