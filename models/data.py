import json
from pathlib import Path

users_db: list["BaseUser"] = []
USER_FILE = "./data/users.json"

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
            
            try:
                user = cls(
                    user["id"],
                    user["name"],
                    user["user_name"],
                    user["email"],
                    user["role"],
                    user["password"],
                    user["country"]
                )
            except ValueError as e:
                print(f"[WARN] Skipped duplicate or invalid user {user["id"]}: {e}")