#super market billing operation

a=input("enter your name:")
b=input("enter your phone number:")
c=input("enter your no.of.items.purchas:")
d=input("enter your total amount:")
        
class shopping:
    customer_name=a
    phone_no=b
    no_of_item_purchas=c
    total_amount=d
    def bill(self):
        print("===========shopping payment bill=====================")
        print("customet name:",self. customer_name)
        print("phone no:",self.phone_no)
        print("no_of_item_purchas:",self.no_of_item_purchas)
        print("total amount:",self.total_amount)
        
s=shopping()
s.bill()
