import argparse
from utils.utils import user_auth, user_logout
from models.data import load_users_from_file, users_db
from models.session import session

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

if __name__ == "__main__":
    main()