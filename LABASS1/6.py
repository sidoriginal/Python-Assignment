b=int(input("Enter basic pay:"))
print("Salary: ")
if b<=10000:
    print(b+0.2*b+0.8*b)
elif  b<=20000 and b>=10000:
    print(b+0.25*b+0.9*b)
else:
    print(b+0,3*b+0.95*b)