import math
x=int(input("Enter x"))
n=int(input("Enter n"))
s=1;
for i in range(1,n+1):
    j=math.pow(x,i)/math.factorial(i);
    print(j);
    s=s+j;
print(s);

