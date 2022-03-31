MIN_LENGTH = 6
MAX_LENGTH = 15


def main():
    """Program to get and check user's password"""
    password = input("Please enter you new password: ")
    while not is_valid_password(password):
        print(f"Invalid password: Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters")
        password = input("Please enter you new password: ")
    display_asterisk(password)


def display_asterisk(password):
    for char in password:
        print("*", end=" ")


def is_valid_password(password):
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    return True


main()