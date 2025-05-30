from users import BaseUser, AdminUser, users

admin_user = AdminUser(0, "Admin", "admin", "admin1234", "")
regular_user = BaseUser(1, "Batman", "user", "TheDarkKnight123", "US")
test_user = BaseUser(2, "John Doe", "user", "hello123", "US")

if __name__ == '__main__':
    regular_user.show_info()
    admin_user.update_user(2, {"user_role": "test"})
    admin_user.get_user_info(2)