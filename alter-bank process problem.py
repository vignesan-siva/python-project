
print("===============WELCOME TO ABC BANK======================")
print("")
print("")


print("================Login Page==================")
user_name=input("Enter You User Name:")
password=(int(input("Enter You password:")))
          #user_name:vignesan
          #password:123
if user_name=="vignesan" and password==123:
    print("welcome to abc bank")
else:
    print("user_name or password incorrect")

#credit process
print("===========credit process====================")
credit=[]
d=credit
i=int(input("enter credit amount:"))
credit.append(i)
print("account balance:",d)
a=int(input("enter depit amount:"))
print("===============depit process==================")
depit=[a]
if credit[0]>=depit[0]:
   
   print("depited amount:",a)
else:
    print("invalid balance on your account")
print("================Total amount on account============")
if credit[0]>=depit[0]:
    d=credit[0]-depit[0]
    print("total balance:",d)
else:
    e=credit[0]
    print("total balance:",e)































