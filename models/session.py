from typing import Optional

class Session:
    def __init__(self):
        self._logged_user: Optional["BaseUser"] = None
    
    def login(self, user: "BaseUser") -> None:
        self._logged_user = user
        print(f"{user.user_name} logged in.")
    
    def logout(self) -> None:
        print(f"{self._logged_user.user_name} logged out.")
        self._logged_user = None
    
    def current_user(self) -> Optional["BaseUser"]:
        return self._logged_user
    
    def is_authenticated(self) -> bool:
        return self._logged_user is not None
    
session = Session()