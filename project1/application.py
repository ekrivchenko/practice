import uuid
from project1.base_objects import *
from project1.utils import Utils
import json
import time


class Response:
    def __init__(self, status_code, body):
        self.status_code = status_code
        self.body = body


class UserOperations:
    def __init__(self):
        self.users = dict()
        self.utils = Utils()

    def create_user(self, first_name, last_name, email, phone):
        print('Creating user with email: {0} ...'.format(email))
        generated_uuid = self.utils.generate_uuid()
        print('Generated uuid {0}'.format(generated_uuid))
        user = User(first_name, last_name, email, phone, uuid1=generated_uuid)
        print('User {0} was successfully created and uuid {1} assigned!'.format(user.email, user.uuid))

        with open('users.json', 'a') as f:
            print('File opened...')
            f.write(json.dumps(user.__dict__))

        print('File was closed...')
        self.users[user.uuid] = user

    def get_user_by_email(self, email):
        for user in self.users:
            if self.users[user].email == email:
                return Response(200, self.users[user])
        return Response(404, 'Not Found')


user_operations = UserOperations()


user_operations.create_user(first_name='Ilya', last_name='Stepanko', email='ilya.email@icloud.com', phone=7189097106)
time.sleep(2)

user_operations.create_user(first_name='Eugene', last_name='Krivchenko', email='eugene.krivchenko@gmail.com',
                            phone=4087184002)

resp = user_operations.get_user_by_email(email='ilya.email@icloud.co1m')
if resp.status_code == 200:
    print(resp.body.first_name)
