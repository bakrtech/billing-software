from modules.admin import *
import os
user = login()
os.system("clear")
if user =="ADMIN":
    print("YOU ARE AN ADMIN")
else:
    print("JUST ANOTHER NORMIE UWU")
