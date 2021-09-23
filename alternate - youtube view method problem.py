n=(int(input("enter youtube view:")))
if n<1000:
    print(n)
elif n<=10000000:
     print(n/1000,"K","views")
elif n<=1000000000:
     print(n/10000000,"M","views")
elif n<=1000000000000:
     print(n/1000000000,"B","views")  
else:
    print("sorry,try again")
