def left(init,pos):
    ans=""
    for i in init:
        if i==init[pos-1]:
            ans+=init[pos]
        elif i==init[pos]:
            ans+=init[pos-1]
        else:
            ans+=i
    return ans


def right(init,pos):
    ans=""
    for i in init:
        if i==init[pos+1]:
            ans+=init[pos]
        elif i==init[pos]:
            ans+=init[pos+1]
        else:
            ans+=i
    return ans


def up(init,pos):
    ans=""
    for i in init:
        if i==init[pos-3]:
            ans+=init[pos]
        elif i==init[pos]:
            ans+=init[pos-3]
        else:
            ans+=i
    return ans


def down(init,pos):
    ans=""
    for i in init:
        if i==init[pos+3]:
            ans+=init[pos]
        elif i==init[pos]:
            ans+=init[pos+3]
        else:
            ans+=i
    return ans


init='123804765'
fin='281043765'
q=[init]
d={}
count=0

while (len(q)>0):
    cl=q[0]
    if(cl==fin):
        break
    pos=int(cl.find('0'))
    if(pos!=0 and pos!=3 and pos!=6):
        count+=1
        r=left(cl,pos)
        if r not in d.keys():
            d[r]=cl
            q.append(r)
    if(pos!=2 and pos!=5 and pos!=8):
        count+=1
        r=right(cl,pos)
        if r not in d.keys():
            d[r]=cl
            q.append(r)
    if(pos!=6 and pos!=7 and pos!=8):
        count+=1
        r=down(cl,pos)
        if r not in d.keys():
            d[r]=cl
            q.append(r)
    if(pos!=0 and pos!=1 and pos!=2):
        count+=1
        r=up(cl,pos)
        if r not in d.keys():
            d[r]=cl
            q.append(r)
    q.pop(0)
cl=fin
result=[fin]
while cl!=init:
    result.insert(0,d[cl])
    cl=d[cl]
# print(result)
for i in result:
    print(i[0:3],end=" ")
print("\n",end="")
for i in result:
    print(i[3:6],end=" ")
print("\n",end="")
for i in result:
    print(i[6:9],end=" ")

            
            
        
