from models.session import session
from models.data import users_db
from typing import Optional
import secrets
import string

def user_auth(user_name: str, password: str) -> Optional["BaseUser"]:
    for user in users_db:
        logged_user = session.current_user
        if logged_user and logged_user.user_name == user_name:
            print("[ERROR] User already logged in.")
            return
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

def generate_user_id() -> int:
    if not users_db:
        return 0
    return max(user.user_id for user in users_db) + 1

def generate_password(length: int = 12) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))