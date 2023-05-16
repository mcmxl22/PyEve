import getpass
import hashlib
import os
import pickle

class UserAccount:
    """
    A class representing a user account with login and registration features.
    """
    
    def __init__(self):
        # Load user data from a file if it exists
        self.user_data = {}
        self.user_data_file = 'user_data.pkl'
        if os.path.exists(self.user_data_file):
            with open(self.user_data_file, 'rb') as f:
                self.user_data = pickle.load(f)

    def hash_password(self, password):
        """Return the SHA-256 hash of the password."""
        return hashlib.sha256(password.encode()).hexdigest()

    def register_account(self):
        """Register a new user account."""
        username = input("\nEnter username: ")

        # Check if the username is already in use
        if username in self.user_data:
            print("Username is already in use.")
            return False

        while True:
            password = getpass.getpass("Enter password: ")

            # Check if the password meets the requirements
            if (len(password) >= 8 and
                    any(char.isdigit() for char in password) and
                    any(char.isupper() for char in password) and
                    any(char.islower() for char in password)):
                break
            else:
                print("Password does not meet the requirements. Please try again.")

        # Store the username and hashed password
        self.user_data[username] = self.hash_password(password)

        # Save the user data to a file
        with open(self.user_data_file, 'wb') as f:
            pickle.dump(self.user_data, f)

        print("Account registered successfully.")
        return True

    def login(self):
        """Login to an existing user account."""
        username = input("\nEnter username: ")

        # Check if the username exists
        if username not in self.user_data:
            print("Username does not exist.")
            return False

        password = getpass.getpass("Enter password: ")

        # Check if the password is correct
        if self.user_data[username] != self.hash_password(password):
            print("Incorrect password.")
            return False

        print("Logged in successfully.")
        return True
