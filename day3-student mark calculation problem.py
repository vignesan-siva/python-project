name=input("enter your name:")
sub1=input("enter python mark:")
sub2=input("enter java mark:")
sub3=input("enter machine learning mark:")
sub4=input("enter deep learning mark:")
sub5=input("enter networking mark:")
c=[sub1,sub2,sub3,sub4,sub5]
d=["python","java","machine learning","deep learning","networking"]
print("==========seperate every student mark=================")
#print the student mark an all the subjects separatly
i=0
while i<5:
  print(name,d[i],"mark:",c[i])
  i+=1
#Total mark of student first converted into integer then add otherwise error display
print("==============Total marks=========================")
total=sub1
a=int(total)
t=sub2
b=int(t)
h=sub3
c=int(h)
w=sub4
d=int(w)
f=sub5
e=int(f)
f=a+b+c+d+e
print(name,"total mark:",f)
print("=========average of mark================")
#average of student mark
print(name,"average of mark:",f/5)
print("=========maximum mark=========")
r=max(a,b,c,d,e)
print(name,"maximum of mark",r)
print("==========mimimum mark==========")
r=min(a,b,c,d,e)
print(name,"minimum of mark:",r)
