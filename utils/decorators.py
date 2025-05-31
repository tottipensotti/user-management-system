from functools import wraps
from models.session import session

def requires_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = session.current_user()

        if user is None:
            raise PermissionError("Access denied: No user is logged in.")

        if user.user_role != "admin":
            raise PermissionError(f"Access denied: User {user.user_name} does not have admin privileges.")

        return func(*args, **kwargs)
    return wrapper
