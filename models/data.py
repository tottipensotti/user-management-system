import json
from pathlib import Path

users_db: list["BaseUser"] = []
USER_FILE = "./data/users.json"
USER_DATABASE = ".users"

def load_users_from_file(file_path: str = USER_FILE):
    from models.users import BaseUser, AdminUser
    users_db.clear()
    path = Path(file_path)

    if not path.exists():
        print(f"[INFO] File {file_path} not found.")
        return
    
    with open(path, "r") as f:
        data = json.load(f)
        for user in data:
            role = user.get("role")
            cls = AdminUser if role == "admin" else BaseUser
            pwd = None
            if role == "admin":
                pwd = "admin"
            elif role == "test":
                pwd = "test"

            try:
                cls(
                    name = user["name"],
                    user_name = user["user_name"],
                    email = user["email"],
                    country = user["country"],
                    role = user["role"],
                    pwd = pwd
                )
            except ValueError as e:
                print(f"[WARN] Skipped duplicate or invalid user {user["user_name"]}: {e}")

def save_users_to_file(file_path: str = USER_DATABASE):
    path = Path(file_path)

    try:
        user_dicts = [user.__dict__ for user in users_db]

        with open(path, "w") as f:
            json.dump(user_dicts, f, indent=4)

        print(f"[INFO] User database successfully saved in {file_path}.")
    except Exception as e:
        print(f"[ERROR] Failed to save user database: {e}")