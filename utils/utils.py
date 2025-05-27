from users import User

users = [
    User(1, "John", "user", "1234", "Fake Street 123"),
    User(2, "Bob", "user", "abcd1234", "Somewhere Over The Rainbow 123"),
    User(3, "Alice", "user", "cats4ever", "Time Square 1"),
    User(4, "Satoshi", "user", "btc100", "Nowhere 123"),
    User(5, "Greg", "user", "securepassword", "Av. Siempreviva 123")
]

def create_new_user(id: int, name: str, pwd: str, address: str, role: str = "user") -> dict:
    for user in users:
        if user.user_id == id:
            raise ValueError("User Already exists")
    
    new_user = User(id, name, role, pwd, address)
    print(f"Succesfully created user {new_user.user_id}.")
    return new_user

def get_user_info(user_id: int) -> dict:
    for user in users:
        if user.user_id == user_id:
            return user.__dict__
    
    raise ValueError(f"User {user_id} not found.")

def update_user(user_id: int, new_info: dict ) -> dict:
    for i, user in enumerate(users):
        if user.user_id == user_id:
            user_index: int = i

    for key in new_info:
        users[user_index].__dict__[key] = new_info[key]

    print(f"Succesfully updated user {user_id}.")

    raise ValueError(f"User doesn't exists.")

def delete_user(user_id: int) -> None:
    for i, user in enumerate(users):
        if user.user_id == user_id:
            index: int = i
    users.remove(users[index])
    print(f"Succesfully deleted user {user_id}.")
    
    raise ValueError(f"User doesn't exists.")
