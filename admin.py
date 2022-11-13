import pickle
credintials = open("Backend/.admin.dat","rb")
information=pickle.load(credintials)
username=information[0]
password=information[1]
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
login()
credintials.close()