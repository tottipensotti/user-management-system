from models.session import session
from models.users import BaseUser, users_list
from typing import Optional, Callable
from functools import wraps

def user_auth(user_name: str, password: str) -> Optional[BaseUser]:
    for user in users_list:
        if user.user_name == user_name and user.check_password(password):
            session.login(user)
            return user
    raise ValueError("Incorrect user_name and/or password. Try again.")

def user_logout(user_name: str) -> None:
    logged_user = session.current_user()
    if logged_user.user_name == user_name:
        session.logout()
        return
    raise ValueError("Problem while logging out. Try again.")