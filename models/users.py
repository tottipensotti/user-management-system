from utils.decorators import requires_auth
from utils.utils import generate_user_id, generate_password
from models.data import users_db

class BaseUser:
    def __init__(self, name: str, user_name: str, email: str, country: str, role: str, pwd: str = None):
        global users_db
        if any(user.user_name == user_name for user in users_db):
            print(f"[ERROR] User {user_name} already exists.")

        self.user_id: int = generate_user_id()
        self.name: str = name
        self.user_name: str = user_name
        self.user_email: str = email
        self.user_role: str = role
        self.country: str = country
        self.__password: str = pwd if pwd else generate_password()
        users_db.append(self)
    
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
    def __init__(self, name: str, user_name: str, email: str, country: str, role: str = "admin", pwd: str = "admin"):
        super().__init__(name, user_name, email, country, role, pwd)

    @requires_auth
    def create_user(self, name: str, user_name: str, email: str, country: str, role: str = "user", pwd: str = None):
        global users_db
        if any(user.user_name == user_name for user in users_db):
            print(f"[ERROR] User {user_name} already exists.")
            return
        
        cls = AdminUser if role == "admin" else BaseUser    
        
        try:
            cls(
                name=name,
                user_name=user_name,
                email=email,
                country=country,
                role=role,
                pwd=pwd
            )
            print(f"[INFO] User {user_name} successfully created.")
        except ValueError as e:
            print(f"[ERROR] {e}")

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
        elif user_email:
            for user in users_db:
                if user.user_email == user_email:
                    user.show_info()
                    return
        elif user_name:
            for user in users_db:
                if user.user_name == user_name:
                    user.show_info()
                    return
        else:
            print("[ERROR] At least one attribute is needed to search (user_id, user_name, user_email).") 