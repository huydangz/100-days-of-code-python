from twilio.rest import Client

TWILIO_SID = "AC2915a8b4dcb2e78be04319ecda8f4446"
TWILIO_TOKEN = "2eda7e0387d9f22d78c48ed024d920b4"
FROM = "+13025644808"
TO = "+84977201771"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_sms(self, sms):
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        message = client.messages.create(body=sms, from_=FROM, to=TO)
        print(message.status)