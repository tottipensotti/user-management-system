class BaseUser:
    def __init__(self, id, name, role, pwd, country):
        if any(user.user_id == id for user in users):
            raise ValueError(f"User ID {id} already exists.")
        
        self.user_id: int = id
        self.user_name: str = name
        self.user_role: str = role
        self._password: str = pwd
        self.country: str = country
        users.append(self)
        print(f"User {self.user_id} successfully created.")

    def greet(self) -> None:
        print(f'Hello! My name is {self.user_name}')
    
    def show_info(self) -> str:
        user_info = (
            "----------------------------------------\n"
            "User information\n"
            "----------------------------------------\n"
            f"- User ID: {self.user_id}\n"
            f"- Name: {self.user_name}\n"
            f"- Country: {self.country}\n"
        )
        print(user_info)

class AdminUser(BaseUser):
    def __init__(self, id, name, role, pwd, country):
        super().__init__(id, name, role, pwd, country)

    def update_user(self, user_id: int, new_info: dict) -> None:
        for i, user in enumerate(users):
            if user.user_id == user_id:
                for key in new_info:
                    if hasattr(user, key):        
                        setattr(users[i], key, new_info[key])
                    else:
                        e: str = f"{key} is not a valid attribute."
                        raise ValueError(e)
                print(f"Successfully updated user {user_id}.")
                return

        raise ValueError("User doesn't exist.")

    
    def delete_user(self, user_id: int) -> None:
        for i, user in enumerate(users):
            if user.user_id == user_id:
                index: int = i
        users.remove(users[index])
        print(f"Succesfully deleted user {user_id}.")
        
        raise ValueError("User doesn't exists.")

    def get_user_info(self, user_id: int) -> dict:
        for user in users:
            if user.user_id == user_id:
                return user.__dict__
    
users: list[BaseUser] = []