from utils.decorators import requires_auth
from models.data import users_db

class BaseUser:
    def __init__(self, id: int, name: str, user_name: str, email: str, role: str, pwd: str, country: str):
        global users_db
        if any(user.user_id == id for user in users_db):
            print(f"[ERROR] User ID {id} already exists.")
        
        self.user_id: int = id
        self.name: str = name
        self.user_name: str = user_name
        self.user_email: str = email
        self.user_role: str = role
        self.__password: str = pwd
        self.country: str = country
        users_db.append(self)
        print(f"[INFO] User {self.user_id} successfully created.")
    
    def show_info(self) -> str:
        user_info = (
            "----------------------------------------\n"
            "User information\n"
            "----------------------------------------\n"
            f"- User ID: {self.user_id}\n"
            f"- Name: {self.name}\n"
            f"- Username: {self.user_name}\n"
            f"- Email: {self.user_email}\n"
            f"- Country: {self.country}\n"
        )
        print(user_info)

    def check_password(self, pwd: str) -> bool:
        return self.__password == pwd

class AdminUser(BaseUser):
    def __init__(self, id: int, name: str, user_name: str, email: str, role: str, pwd: str, country: str):
        super().__init__(id, name, user_name, email, role, pwd, country)

    @requires_auth
    def create_user(self, user_id: int, name: str, user_name: str, email: str, pwd: str, country: str, role: str = "user"):
        global users_db
        if any(user.user_id == user_id for user in users_db):
            print(f"[ERROR] User ID {user_id} already exists.")
        
        new_user = BaseUser(user_id, name, user_name, email, role, pwd, country)
        users_db.append(new_user)

        print(f"[INFO] User {user_id} successfully created.")

    @requires_auth
    def update_user(self, user_id: int, new_info: dict) -> None:
        global users_db
        for i, user in enumerate(users_db):
            if user.user_id == user_id:
                for key in new_info:
                    if hasattr(user, key):        
                        setattr(users_db[i], key, new_info[key])
                    else:
                        e: str = f"{key} is not a valid attribute."
                        print(f"[ERROR] {e}")
                print(f"[INFO] Successfully updated user {user_id}.")
                return

        print("[ERROR] User doesn't exist.")
    
    @requires_auth
    def delete_user(self, user_id: int) -> None:
        global users_db
        for i, user in enumerate(users_db):
            if user.user_id == user_id:
                index: int = i
        users_db.remove(users_db[index])
        print(f"[INFO] Succesfully deleted user {user_id}.")
        
        print("[ERROR] User doesn't exists.")

    @requires_auth
    def get_user_info(self, user_id: int, user_email: str, user_name: str) -> dict:
        if user_id:
            for user in users_db:
                if user.user_id == int(user_id):
                    user.show_info()
                    return
        if user_email:
            for user in users_db:
                if user.user_email == user_email:
                    user.show_info()
                    return
        if user_name:
            for user in users_db:
                if user.user_name == user_name:
                    user.show_info()
                    return
        else:
            print("[ERROR] At least one attribute is needed to search (user_id, user_name, user_email).")