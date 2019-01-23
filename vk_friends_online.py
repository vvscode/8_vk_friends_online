import vk
import os
import sys
import getpass

APP_ID = os.environ.get('VK_APP_ID')
API_VERSION = 5.73

def get_user_login():
    return input("Login: ")


def get_user_password():
    return getpass.getpass("Password: ")


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    online_friends_ids = list(api.friends.getOnline(v=API_VERSION))
    if not online_friends_ids:
        return []

    user_ids_string = ','.join(map(str, online_friends_ids))
    online_friends = api.users.get(user_ids=user_ids_string,v=API_VERSION)
    return online_friends


def output_friends_to_console(friends_online):
    print("You have {} friend(s) online".format(len(friends_online)))
    for friend in friends_online:
        print("# {id} - {first_name} {last_name}".format(**friend))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()

    try:
        friends_online = get_online_friends(login, password)
    except vk.exceptions.VkAuthError:
        sys.exit("Use correct login/password")

    output_friends_to_console(friends_online)
