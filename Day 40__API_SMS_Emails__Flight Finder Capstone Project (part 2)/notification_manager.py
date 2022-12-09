from twilio.rest import Client
import smtplib

TWILIO_SID = "AC2915a8b4dcb2e78be04319ecda8f4446"
TWILIO_TOKEN = "2eda7e0387d9f22d78c48ed024d920b4"
FROM = "+13025644808"
TO = "+84977201771"
MY_EMAIL = "lamasia30@gmail.com"
MY_PASSWORD = "zwtmosuqijrdvyam"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_sms(self, sms):
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        message = client.messages.create(body=sms, from_=FROM, to=TO)
        print(message.status)

    def send_email(self, list_emails):
        with smtplib.SMTP("smtp.gmail.com", 587) as conn:
            conn.starttls()
            conn.login(user=MY_EMAIL, password=MY_PASSWORD)
            for email in list_emails:
                conn.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email["email"],
                    msg=f'Subject:New Low Price Flight!\n\n{email["message"]}'.encode('utf-8')
                )
