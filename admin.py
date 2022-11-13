username="admin".lower()
password="thesafestpassword".lower()
print("Admin login ")
username_in = input("Enter your username: ")
password_in = input("Enter your password: ")
if username_in==username and password_in==password:
    print("login Succesfully")

