'''
append item 
remove ''
calc
product info


>CODE 
display infor mationa
.
.
.
.
.
.
Number of titma n stocks =21
Quantiy > 2
ADDING {quantity} * XYZ in bill
CONFIRM >y/n
add
1) item one
...

..
6) item six
enter the number
> 6
Do you want to remove all or <quantity
'''
def adding_an_item(bill):
    item_code=input('Enter the code of the item added: ')
    print('Product information')
    if item_code in file:
        pass
    x=int(input('Enter the no. of items u want: '))
    cfming=input('Do you really want to add ',item_name,'and',x,'items? (y/n)')
    if cfming=='y':
        bill[item_code]=x
    print('Successfully added!')    

def display_bill(bill):
    for key,value in bill:
        print('')
            
        


