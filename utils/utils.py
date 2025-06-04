from models.session import session
from models.users import BaseUser, AdminUser
from models.data import users_db
from typing import Optional

def user_auth(user_name: str, password: str) -> Optional[BaseUser]:
    for user in users_db:
        logged_user = session.current_user
        if logged_user and logged_user.user_name == user_name:
            print("[ERROR] User already logged in.")
        if user.user_name == user_name and user.check_password(password):
            session.login(user)
            return user
    print("[ERROR] Incorrect user_name and/or password. Try again.")

def user_logout(user_name: str) -> None:
    logged_user = session.current_user

    if not logged_user:
        print("[INFO] No user is currently logged in.")
    if logged_user.user_name == user_name:
        session.logout()
        return
    print("[ERROR] Problem while logging out. Try again.")

def create_default_admin():
    if not any(user.user_name == "admin" for user in users_db):
        admin = AdminUser(0, "admin", "admin@admin.com", "admin", "admin", "HQ")
        users_db.append(admin)