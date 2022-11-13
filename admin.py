username="admin".lower()
password="thesafestpassword".lower()
print("Admin login ")
def login():
    username_in = input("Enter your username: ")
    password_in = input("Enter your password: ")
    if username_in==username and password_in==password:
        print("loged in as ADMIN")
        return "ADMIN"
    else:
        print(f"Loged in as {username_in}")
        return str(username_in)

