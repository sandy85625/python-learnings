import re

"""
Create a Class for to check validity of a given username and password. It implements functions:
 - validate_username
 - validate_password
"""
class Validator:
    def __init__(self):
        # Regular expressions for username and password validation
        self.USERNAME_REGEX = r"^[a-zA-Z][a-zA-Z0-9]*([.][a-zA-Z0-9]*)?@gecskp\.ac\.in$"
        self.PASSWORD_REGEX = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&/])[A-Za-z\d@$!%*#?&/]{8,}$"


    def validate_username(self, username):
        if not re.match(self.USERNAME_REGEX, username):
            print("\nInvalid username!")
            return False
        return True

    def validate_password(self, password):
        if not re.match(self.PASSWORD_REGEX, password):
            print("\nInvalid password!")
            return False
        return True

validator = Validator()

while True:
    print("======================================")
    print("\nValidate Username and Password")
    print("\n- Username must start with alphabet and should have only one period, and it should end with @gecskp.ac.in.")
    print("- Password should contain atleast 8 characters and should have atleast one alphabet, one numeric, and one special character @, $, /.")
    username = input("\nEnter username: ")
    password = input("Enter password: ")

    print(username, password)

    valid_username = validator.validate_username(username)
    valid_password = validator.validate_password(password)

    if valid_username and valid_password:
        print("\nLogin successful!")
    else:
        print("Login failed.")

