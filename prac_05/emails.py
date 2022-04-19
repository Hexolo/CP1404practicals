
def get_name():
    name = email.split("@")[0]
    name = name.split(".")
    name = " ".join(name)
    email_to_name[email] = name.title()


email_to_name = {}
email = input("Email: ")
while email != "":
    get_name()
    name_confirmation = input(f"Is your name {email_to_name[email]}? (Y/N) ").lower()
    if name_confirmation == "y" or name_confirmation == "" or name_confirmation == "yes":
        email = input("Email: ")
    else:
        email_to_name[email] = input("Name: ")
        email = input("Email: ")
for email, name in email_to_name.items():
    print(f"{name} ({email})")