from project1.UtilsClass import *
from project1.UserClass import *
import json

class UserOperations:
    def __init__(self):
        self.users = dict()
        self.utils = Utils()

    def get_all_users(self):
        self.load_users()
        return self.users.values()

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

    def change_first_name(self, email):
        new_first_name = input('Please Enter new first name: ')
        for user in self.users:
            if self.users[user].email == email:
                self.users[user].first_name = new_first_name
                print("\nFirst name for that user is changed successfully")
                #code works here... just need to write to file somehow...

    def change_last_name(self, email):
        new_last_name = input('Please Enter new last name: ')
        for user in self.users:
            if self.users[user].email == email:
                self.users[user].last_name = new_last_name
                print("\nLast name for that user is changed successfully")
                # code works here... just need to write to file somehow...

    def change_email(self, email):
        new_email = input('Please Enter new email: ')
        for user in self.users:
            if self.users[user].email == email:
                self.users[user].email = new_email
                print("\nEmail for that user is changed successfully")
                # code works here... just need to write to file somehow...

