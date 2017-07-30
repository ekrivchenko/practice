from project1.base_objects import *
from project1.utils import Utils, Twillio
import json


class Response:
    def __init__(self, status_code, body):
        self.status_code = status_code
        self.body = body


class UserOperations:
    def __init__(self):
        self.users = dict()
        self.utils = Utils()
        self.twillio = Twillio()

    def load_users(self):
        self.users.clear()
        with open('users.txt', 'r') as f:
            for line in f:
                user = json.loads(line)
                self.users[user['uuid']] = User(**user)

    def create_user(self, first_name, last_name, email, phone):
        print('Creating user with email: {0} ...'.format(email))
        generated_uuid = self.utils.generate_uuid()
        print('Generated uuid {0}'.format(generated_uuid))
        user = User(first_name, last_name, email, phone, uuid=generated_uuid)
        print('User {0} was successfully created and uuid {1} assigned!'.format(user.email, user.uuid))

        with open('users.txt', 'a') as f:
            print('File opened...')
            f.write(json.dumps(user.__dict__) + '\n')

        print('File was closed...')
        self.users[user.uuid] = user
        self.twillio.send_text(phone_to=user.phone, text='You created user: {0}'.format(user.__dict__), phone_from='3473281403')

    def get_user_by_email(self, email):
        for user in self.users:
            if self.users[user].email == email:
                return Response(200, self.users[user])
        return Response(404, 'Not Found')

    def delete_user_by_uuid(self, uuid):
        del self.users[uuid]
        with open('users.txt', 'w') as f:
            users = list()
            for user in self.users:
                users.append(json.dumps(self.users[user].__dict__) + '\n')
            f.writelines(users)

    def get_all_users(self):
        return self.users.values()

if __name__ == '__main__':
    user_operations = UserOperations()
    user_operations.load_users()
    while True:
        selection = input('\n1 - Create User\n2 - Find User UUID by email\n3 - Delete User\n4 - Print all users\n\n')
        if selection == '1':
            first_name = input('Enter user first name: ')
            last_name = input('Enter user last name: ')
            email = input('Enter user email: ')
            phone = input('Enter user phone number: ')
            user_operations.create_user(first_name=first_name, last_name=last_name, email=email, phone=phone)
        elif selection == '2':
            email = input('Enter user email to look for: ')
            resp = user_operations.get_user_by_email(email)
            if resp.status_code == 200:
                print('User with email {0} has uuid {1}'.format(email, resp.body.uuid))
            else:
                print('User with email {0} not found.'.format(email))
        elif selection == '3':
            email = input('Enter user email to delete: ')
            resp = user_operations.get_user_by_email(email)
            if resp.status_code != 200:
                print('User with email {0} not found.'.format(email))
            else:
                user_operations.delete_user_by_uuid(resp.body.uuid)
                print('User was senselessly deleted!')
        elif selection == '4':
            users = user_operations.get_all_users()
            for user in users:
                print(user.__dict__)
        else:
            print('Wrong selection, try again.')
