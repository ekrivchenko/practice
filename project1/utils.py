import uuid


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def generate_uuid():
        return str(uuid.uuid4())
