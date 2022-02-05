bas=int(input("Enter basic pay:"))
print("Salary: ")
if bas<=10000:
    print(bas+0.2*bas+0.8*bas)
elif  bas<=20000 and bas>=10000:
    print(bas+0.25*bas+0.9*bas)
else:
    print(bas+0.3*bas+0.95*bas)