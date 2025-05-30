# 🧠 Python User Management System – Practice Project

This project is designed to help you practice and master core Python skills by building an incrementally more complex user management system. You'll simulate a backend system that supports user creation, deletion, updates, and authentication — all through pure Python code (no web frameworks).

## 🛠️ Skills Practiced
- Functions, type hints, and annotations
- Classes and inheritance
- Decorators and encapsulation
- Dictionary and list operations
- Control flow (`if`, `for`, `while`)
- Data validation and exception handling
- OOP design patterns
- Optional: basic persistence with file I/O
---

## Project Roadmap

### Phase 1: Core CRUD Logic
**Focus:** Functions, typing, list/dict manipulation

#### 📌 Goals
- Create a `User` class with the following attributes:
    - `user_id`
    - `user_name`
    - `user_role`
    - `_password` (private)
    - `address`
- Define a global `users` list containing `User` objects
#### 🛠️ Functions to Implement
- `create_new_user()`:  
    Adds a new user to the `users` list, only if the `user_id` is unique.
- `delete_user(user_id)`:  
    Removes a user from the list based on their `user_id`.
- `update_user(user_id, new_info_dict)`:  
    Updates the user's information using key-value pairs from the dictionary.
- `get_user_info(user_id)`:
    Retrieves the user's information.
#### 🖨️ Output/Debugging
- Print user values using:
    - `user.__dict__`, or
    - Define and use a custom `__str__()` method inside the `User` class
---

### 🧱 Phase 2: Object-Oriented Design
**Focus:** Classes, inheritance, cleaner design

#### 📌 Goals
- Refactor the codebase to follow object-oriented principles
- Introduce inheritance to support different types of users
#### 🏗️ Classes to Create
- `BaseUser`:  
    A parent class containing shared attributes and methods for all user types
- `AdminUser` (inherits from `BaseUser`):  
    - May have additional privileges like deleting or managing other users
    - Can override or extend base class methods
- `RegularUser` (inherits from `BaseUser`):  
    - Limited permissions and access
    - Uses default behavior from `BaseUser`
#### 🛠️ Additional Behaviors
- Move shared methods like `greet()` to the `BaseUser` class
- Add role-specific logic:
    - For example, only `AdminUser` can call certain functions like `delete_user()`
---

### 🔐 Phase 3: Authentication & Access Control
**Focus:** Encapsulation, decorators, control flow, secure logic

#### 📌 Goals
- Introduce password-based authentication
- Use decorators to restrict access to protected operations
- Practice encapsulation using private attributes
#### 🛠️ Features to Implement
- **Encapsulation:**
    - Make the password a private attribute (already `_password`, now enforce access control)
    - Prevent direct access or modification from outside the class
- **Authentication Function:**
  - `authenticate_user(user_id: int, password: str) -> bool`
    - Checks if user credentials match
    - Returns `True` or `False`
- **Session Simulation (optional):**
  - Simulate "login" by storing a reference to an `authenticated_user`
  - Use this object in functions requiring authentication
- **Protected Function Decorator:**
  - Create `@requires_auth` decorator
    - Ensures that a user is authenticated before executing a function (e.g., delete or update)
---

### 💾 Phase 4 (Optional): Data Persistence with File I/O
**Focus:** Reading/writing files, serialization, data management
#### 📌 Goals
- Save the current state of users to a file (e.g., JSON)
- Load users from a file on program start
- Maintain data consistency between sessions
#### 🛠️ Features to Implement
- **Serialization:**
    - Convert `User` objects to dictionaries suitable for JSON serialization
    - Handle private fields properly (e.g., exclude or encrypt passwords)
- **File Writing:**
    - Write the list of users to a JSON file (`users.json`)
    - Save changes after create, update, or delete operations
- **File Reading:**
    - Load users from the JSON file at program start
    - Convert dictionaries back into `User` objects
- **Data Integrity:**
    - Handle cases where the file is missing or corrupted gracefully
#### Bonus Ideas
  - Encrypt passwords before saving
  - Implement backup and restore functionality
  - Support exporting user data in other formats (e.g., CSV)
---
### 🎛️ Phase 5 (Optional): Command-Line Interface (CLI)
**Focus:** Input handling, loops, user interaction, error handling
#### 📌 Goals
- Build a simple text-based CLI to interact with the user management system
- Allow users to:
    - Create new users
    - Authenticate/login
    - Update user details
    - Delete users
    - View all users
#### 🛠️ Features to Implement
- Use an input loop (`while True`) to continuously prompt the user for commands
- Parse and validate user input for each action
- Call the underlying CRUD and auth functions based on commands
- Handle invalid input and exceptions gracefully
- Provide user-friendly prompts and messages
#### Bonus Ideas
  - Add command history or shortcuts
  - Mask password input (e.g., using `getpass` module)
  - Persist CLI session state (e.g., currently logged-in-user)
  - Add help commands and command descriptions
