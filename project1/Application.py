from project1.UserOperations import *

if __name__ == '__main__':
    user_operations = UserOperations()
    user_operations.load_users()

    while True:
        selection = input('\n1 - Create User\n2 - Find User UUID by email\n3 - Delete User\n4 - Print all users\n'
                          '5 - Change User info\n\n')
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
            email = input('Enter user email to delete user: ')
            resp = user_operations.get_user_by_email(email)
            if resp.status_code != 200:
                print('User with email {0} not found.'.format(email))
            else:
                user_operations.delete_user_by_uuid(resp.body.uuid)
                print('\nUser was successfully deleted!')
        elif selection == '4':
            users = user_operations.get_all_users()
            for user in users:
                print(user.__dict__)
        elif selection == '5':
            email = input('Enter user email to change user info: \n')
            resp = user_operations.get_user_by_email(email)
            if resp.status_code != 200:
                print('User with email {0} not found.'.format(email))
            else:
                change_choice = input('User is found, what would you like to change?\n\n1 - change First Name\n2 - cbange Last name'
                      '\n3 - change email\n\n')
                if change_choice == '1':
                    user_operations.change_first_name(email)
                elif change_choice == '2':
                    user_operations.change_last_name(email)
                elif change_choice == '3':
                    user_operations.change_email(email)
                else:
                    print("Wrong selection!")
        else:
            print('Wrong selection, try again.')

