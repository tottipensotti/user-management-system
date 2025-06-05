import json
import argparse
from pathlib import Path
from utils.utils import user_auth, user_logout
from models.data import load_users_from_file, save_users_to_file, users_db, USER_DATABASE
from models.session import session
from models.users import BaseUser, AdminUser

db_path = Path(USER_DATABASE)

if Path(db_path).exists():
    with open(Path(db_path), "r") as f:
        data = json.load(f)
    
    users = []

    for user in data:
        pwd = user.get("_BaseUser__password", "")
        user_dict = {
            "name": user["name"],
            "user_name": user["user_name"],
            "email": user["user_email"],
            "role": user.get("user_role", "user"),
            "pwd": pwd,
            "country": user["country"]
        }

        if user_dict["role"] == "admin":
            user = AdminUser(**user_dict)
        else:
            user = BaseUser(**user_dict)

        users.append(user)
    
    users_db.clear()
    users_db.extend(users)
else:
    load_users_from_file()

def main():
    parser = argparse.ArgumentParser(description="CLI tool to handle user database management.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    login = subparsers.add_parser("login", help="Login as admin user.")
    login.add_argument("-u","--user", required=True, help="Admin username.")
    login.add_argument("-pwd", "--password", required=True, help="Admin user password.")

    logout = subparsers.add_parser("logout", help="End session for current user.")
    logout.add_argument("-u", "--user", required=True, help="Admin username.")

    show_user_info = subparsers.add_parser("show", help="Show information of a specific user.")
    show_user_info.add_argument("-u", "--user", required=False, help="User name.")
    show_user_info.add_argument("-em", "--email", required=False, help="User email.")
    show_user_info.add_argument("-id", "--user_id", required=False, help="User ID.")

    down = subparsers.add_parser("down", help="End session and save users database in JSON.")
    down.add_argument("-p", "--path", required=False, help="Desired path to create the JSON.")

    create_user = subparsers.add_parser("create", help= "Create new user.")
    create_user.add_argument("-n", "--name", required=True, help="User's name.")
    create_user.add_argument("-u", "--username", required=True, help="User's username.")
    create_user.add_argument("-e", "--email", required=True, help="User's email.")
    create_user.add_argument("-r", "--role", required=True, help="User's role.")
    create_user.add_argument("-c", "--country", required=True, help="User's country.")
    create_user.add_argument("-p", "--password", required=False, help="User's default password.")

    args = parser.parse_args()

    if args.command == "login":
        user_auth(args.user, args.password)
    
    if args.command == "logout":
        user_logout(args.user)

    if args.command == "show":
        if session.current_user is None:
            print("[ERROR] No user is currently logged in.")
            return
        if session.current_user.user_role != "admin":
            print("[ERROR] Access denied: Only admin users can view other users info.")
            return
        try:
            for user in users_db:
                if session.current_user.user_id == user.user_id and user.user_role == "admin":
                    user.get_user_info(args.user_id, args.email, args.user)
        except Exception as e:
            print(f"[ERROR] {e}")
    
    if args.command == "create":
        if session.current_user is None:
            print("[ERROR] No user is currently logged in.")
            return
        if session.current_user.user_role != "admin":
            print("[ERROR] Access denied: Only admin users can view other users info.")
            return

        try:
            session.current_user.create_user(
                name=args.name,
                user_name=args.username,
                email=args.email,
                country=args.country,
                role=args.role,
                pwd=args.password
            )
            save_users_to_file()
        except Exception as e:
            print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()