n1=12
n2=8
n3=5
x=n1
y=0
z=0
t=6
d1=0
d2=0
state=[[x,y,z]]
while(d1!=t or d2!=t):
   if(z==n3):
       z=0
       x=x+n3
       d1=x
       d2=y
       state.append([x,y,z])
    #    print(d1,d2)
    #    print(state)
   elif(y==0):
       if(x<=n2):
           y=x
           x=0
       else:
           y=n2
           x=x-n2
       d1=x
       d2=y
       state.append([x,y,z])
    #    print(d1,d2)
    #    print(state)
   else:
       temp=n3-z
       if(y<=temp):
           z=z+y
           y=0
       else:
           z=z+temp
           y=y-temp
       d1=x
       d2=y
       state.append([x,y,z])
    #    print(d1,d2)
    #    print(state)
        
    
    
     
    
print(state)