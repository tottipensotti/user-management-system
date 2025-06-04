from functools import wraps
from models.session import session

def requires_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = session.current_user

        if user is None:
            print("[WARN] Access denied: No user is logged in.")

        if user.user_role != "admin":
            print(f"[WARN] Access denied: User {user.user_name} does not have admin privileges.")

        return func(*args, **kwargs)
    return wrapper
