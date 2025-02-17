import re
#import os  

class PasswordManager:
    def __init__(self, filename="passwords.txt"):
        self.filename = filename

    def check_strength(self, password):
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if re.match(pattern, password):
            return "Strong password"
        return "Weak password - Use at least 8 characters, including uppercase, lowercase, numbers, and special symbols."

    def save_password(self, website, username, password):
        try:
            with open(self.filename, "a") as file:
                file.write(f"{website} | {username} | {password}\n")
            print("Password saved successfully!")
        except IOError:
            print("Error: Could not save the password.")

    def retrieve_passwords(self):
        try:
            with open(self.filename, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            print("No saved passwords found.")
            return []

if __name__ == "__main__":
    manager = PasswordManager()
    
    while True:
        print("\n1. Check Password Strength")
        print("2. Save Password")
        print("3. View Saved Passwords")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            password = input("Enter password to check: ")
            print(manager.check_strength(password))
        elif choice == "2":
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            manager.save_password(website, username, password)
        elif choice == "3":
            passwords = manager.retrieve_passwords()
            for line in passwords:
                print(line.strip())
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")
