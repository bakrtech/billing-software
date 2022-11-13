import pickle
def Inofrmation():
    Info = open("Backend/information.dat","ab")
    Store_Name = str(input("Enter the store ID :"))
    Store_Mobile_No=str(input("Enter the Store Moblie number: "))
    Store_Address=input('Enter the Store Address: ')
    Store_GSTID=input('Enter GST invoice id: ')
    Store_Disclaimer=input('Enter the Disclaimer for the store :')
    pickle.dump([Store_Name,Store_Mobile_No,Store_Address,Store_GSTID,Store_Disclaimer],Info)
    Info.close()
Inofrmation()
'''
1) Billing page  
2) Stonks
3)Online users
4)exit 
'''