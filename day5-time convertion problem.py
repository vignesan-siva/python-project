#only enter valid number otherwise not properly respond
#hours to second
print("==========1) hours to second==========")
hr=int(input("enter no of hours:"))
def convert(hr):
    hour=hr*60
    return hour
print("second:",convert(hr)) 
#minutes to hour
print("=============2) minutes to hour==================")
minute=int(input("enter no of minutes:"))
a=minute//60
print(a,"hours")
# #second to hour
print("==============3) second to hour==================")
second=int(input("enter no of second:"))
b=second//3600
print(b,"hour")

#hours to second
print("===================4) hour to second============")
d=int(input("enter no of hours:"))
def second(s):
    hd=3600*s
    return hd
print(second(d),"second")

#day to year
print("===============5)day to year=============")
day=int(input("enter no of day:"))
day_to_year=day/365
print("%.2f"%day_to_year,"year")

#year to date
print("===========6)year to date============")
year=int(input("enter no of year:"))
year_to_date=year*365
print("%.0f"%year_to_date,"date")

#month to day
print("===========7)month to day================")
hello=int(input("enter no of month:"))
year=hello*30+5
print("%.0f"%year,"days")

#day-to month
print("==============8)day to month==============")
hi=int(input("enter no of days:"))
month_of=hi//30
print("%.0f"%month_of,"month")

#month to year
print("==============9)month to year==============")
g=int(input("enter no of month:"))
month_of_f=g//12
print("%.0f"%month_of_f,"year")
#year to month
print("==============10)year to month==============")
gu=int(input("enter no of years:"))
month_of_h=gu*12
print("%.0f"%month_of_h,"month")



































