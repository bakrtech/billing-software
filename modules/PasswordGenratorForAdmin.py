import pickle
credintials_file = open("../Backend/.admin.dat","wb")
username =input("Enter the username you want : ")
password = input("Enter the password you want : ")
pickle.dump([username,password], credintials_file)
credintials_file.close()