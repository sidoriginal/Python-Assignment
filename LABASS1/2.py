co=0;
ce=0;
cp=0;
c=0;
for i in range(100,901):
    c=0;
    if(i%2==0):
        print("even:")
        print(i)
        print("\n")
        ce=ce+1;
    if(i%2!=0):
        print("odd:")
        print(i)
        print("\n")
        co=co+1;
    for j in range(1,i+1):
        if(i%j==0):
            c=c+1
    if(c==2):
        print("prime:")
        print(i)
        print("\n")
        cp=cp+1
print("even:")
print(ce)
print("\n")
print("odd:")
print(co)
print("\n")
print("prime:")
print(cp)
print("\n")