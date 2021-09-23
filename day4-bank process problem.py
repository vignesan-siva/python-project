print("===============WELCOME TO ABC BANK======================")
print("")
print("")


print("================Login Page==================")
user_name=input("Enter You User Name:")
password=(int(input("Enter You User Name:")))
          #user_name:vignesan
          #password:123
if user_name=="vignesan" and password==123:
    print("welcome to abc bank")
else:
    print("user_name or password incorrect")
         #credit  process of account
print("")
print("===============Credit Card Details=====================")
b=(100)
print("Balance of your account:",b)
a=(int(input("enter transfer amount:")))
d=b+a
total_amount=[d]#converted number into array format easy way to add total
total=0
for i in total_amount:
    total=total+i
print("updated account balance:",total)
d=(total)
#depit process of account
print("================Depit Card Details================")
b=(int(input("enter depit amount:")))
print("depited amount:",b)
print("")
d=total-b#credit total -depit value

print("==================Total amount of account============")
print("remaining balance:",d)


print("==========payment history===============")

transfer_amount=(int(input("enter transfer amount:")))
user_name=input("enter user_name:")
date=input("enter date:")
branch=input("branch:")
tranfer_account=(int(input("enter transfer amount no:")))
print("==========history=================")
print("transfer_amount:","user_name:","date:","branch:","transfer_acount no:")

print(transfer_amount,"","",user_name,"","",date,"","",branch,"","",tranfer_account)





