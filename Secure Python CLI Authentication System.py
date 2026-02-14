import hashlib

# Class representing a User
class User:
    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash

# Main application
class LoginSystem:
    def __init__(self):
        self.users = []

    def run(self):
        while True:
            self.print_menu()
            choice = input("Select option: ").strip()

            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
            elif choice == "0":
                print("Exiting application...")
                break
            else:
                print("Invalid choice.")

    def print_menu(self):
        print("\n=== SECURE LOGIN SYSTEM ===")
        print("1. Register")
        print("2. Login")
        print("0. Exit")

    def register(self):
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        hashed_password = self.hash_password(password)

        self.users.append(User(username, hashed_password))
        print(f"User '{username}' registered successfully.")

    def login(self):
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        hashed_password = self.hash_password(password)

        for user in self.users:
            if user.username == username and user.password_hash == hashed_password:
                print(f"Login successful. Welcome {username}!")
                return

        print("Login failed.")

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()


if __name__ == "__main__":
    app = LoginSystem()
    app.run()
