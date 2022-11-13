import pickle
file = open("Backend/.admin.dat","rb")
r =pickle.load(file)
print(r[1])