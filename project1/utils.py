import uuid
from twilio.rest import Client


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def generate_uuid():
        return str(uuid.uuid4())


class Twillio:
    def __init__(self):
        self.client = Client('AC8516ae68e6b59d5eb2d811eef39695a5', '6568b111da3d6de2858a5321e8e0c97f')

    def send_text(self, phone_to, phone_from, text):
        self.client.api.account.messages.create(to=phone_to, from_=phone_from, body=text)
