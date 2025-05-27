class User:
    def __init__(self, id, name, role, pwd, address):
        self.user_id: int = id
        self.user_name: str = name
        self.user_role: str = role
        self._password: str = pwd
        self.address: str = address

    def greet(self) -> None:
        print(f'Hello! My name is {self.user_name}')
    
    def alter_role(self, new_role: str) -> None:
        self.user_role = new_role
        print(f"User role updated for user {self.user_id}: {self.user_role}")