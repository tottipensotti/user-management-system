from utils.utils import *

if __name__ == '__main__':
    # users.append(create_new_user(6, "Batman", "TheDarkKnight", "Gotham City"))
    print(get_user_info(2))

    update_user(2, {"user_name": "Michael Scott"})
    update_user(9, {"user_role": "admin"})