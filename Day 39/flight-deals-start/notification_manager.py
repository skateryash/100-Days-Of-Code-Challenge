from twilio.rest import Client
TWILIO_ACCOUNT_SID = "AC47746dd1f82ad08a81be014cd2be928e"
TWILIO_AUTH_TOKEN = "3f03092b6bca68e995554dcb8791b372"
TWILIO_NUMBER = "+19014459367"
MY_NUMBER = "+919356776250"


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send_sms(self, message_body):
        # print(message)
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = client.messages \
            .create(
            body=message_body,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER
        )
        print(message.sid)

