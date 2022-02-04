n1=int(input("Enter length of list 1:"))
n2=int(input("Enter length of list 2:"))
l1=[]
l2=[]
print("For list 1:")
for i in range(0,n1):
    ele=input("")
    l1.append(ele)
print("For list 2:")
for i in range(0,n2):
    ele=input("")
    l2.append(ele)
print("Common elements are:")
s1=set(l1)
s2=set(l2)
if(len(s1.intersection(s2))>0):
    print(s1.intersection(s2))
else:
    print("No Common elements")


    