p=input("Enter password: ")
sa=0
la=0
n=0
sp=0
if(len(p)>=6 and len(p)<=16):
    for i in p:
        if(i.isdigit()):
            n=1
        if(i.islower()):
            sa=1
        if(i.isupper()):
            la=1
        if(i=='$' or i=='#' or i=='@'):
            sp=1
if(sp==1 and la==1 and sa==1 and n==1):
    print("VALID")
else:
    print("NOT VALID")
    