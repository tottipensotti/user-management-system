from models.users import BaseUser, AdminUser
from utils.utils import session, user_auth, user_logout

admin_user = AdminUser(0, "admin", "admin", "admin", "HQ")
regular_user = BaseUser(1, "Batman", "user", "TheDarkKnight123", "US")
test_user = BaseUser(2, "John Doe", "user", "hello123", "US")

if __name__ == '__main__':
    test_user.show_info() # Test user information.
    
    user_auth("admin", "admin") # Login as admin
    admin_user.update_user(2, {"user_role": "test"}) # Try @requires_auth decorator
    admin_user.get_user_info(2) # See updated information

    print(session.current_user()) # See active user
    user_logout("admin") # Logout