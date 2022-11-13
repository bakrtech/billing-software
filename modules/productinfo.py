import pickle
with open('../Backend/productinfo.dat','wb') as fh:
    while True:
        a =input("> ")
        if a== "exit":
            break
        else:
            productCODE=input("PRODUCT CODE ")
            productName=input("PRODUCT Name ")
            productprice=input("PRODUCT price ")
            p1= [productCODE,productName,productprice]
            pickle.dump(p1, fh)
    
