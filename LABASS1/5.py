l=int(input("Enter lower limit: "))
u=int(input("Enter uper limit: "))
print("Ans:")
for i in range(l+1,u):
    if(i%4==0):
        print(i)
