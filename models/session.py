import os
from typing import Optional
from models.data import users_db

SESSION_FILE = ".session"
class Session:
    def __init__(self):
        self._logged_user: Optional["BaseUser"] = None

    def login(self, user: "BaseUser") -> None:
        self._logged_user = user
        with open(SESSION_FILE, "w") as f:
            f.write(user.user_name)
        print(f"[INFO] {user.user_name} logged in.")
    
    def logout(self) -> None:
        if os.path.exists(SESSION_FILE):
            os.remove(SESSION_FILE)
        print(f"[INFO] {self._logged_user.user_name} logged out.")
        self._logged_user = None
    
    @property
    def current_user(self) -> Optional["BaseUser"]:
        if self._logged_user:
            return self._logged_user
        
        if os.path.exists(SESSION_FILE):
            with open(SESSION_FILE, "r") as f:
                user_name = f.read().strip()
            
            for user in users_db:
                if user.user_name == user_name:
                    self._logged_user = user
                    return user
        return None
    
    def is_authenticated(self) -> bool:
        return self.current_user is not None
    
session = Session()