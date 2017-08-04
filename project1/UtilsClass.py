import uuid

class Utils:
    def __init__(self):
        pass

    @staticmethod
    def generate_uuid():
        return str(uuid.uuid4())

class Response:
    def __init__(self, status_code, body):
        self.status_code = status_code
        self.body = body
