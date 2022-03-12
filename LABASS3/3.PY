from queue import PriorityQueue
import queue

def right(init,goal,pos,c):
    temp=init[pos]
    init[pos]=init[pos+1]
    init[pos+1]=temp
    cost=0
    for i in range(9):
        if(init[i]==goal[i]):
            cost=cost+1
    return init,cost+c


def left(init,goal,pos,c):
    temp=init[pos]
    init[pos]=init[pos-1]
    init[pos-1]=temp
    cost=0
    for i in range(9):
        if(init[i]==goal[i]):
            cost=cost+1
    return init,cost+c


def up(init,goal,pos,c):
    temp=init[pos]
    init[pos]=init[pos-3]
    init[pos-3]=temp
    cost=0
    for i in range(9):
        if(init[i]==goal[i]):
            cost=cost+1
    return init,cost+c


def down(init,goal,pos,c):
    temp=init[pos]
    init[pos]=init[pos+3]
    init[pos+3]=temp
    cost=0
    for i in range(9):
        if(init[i]==goal[i]):
            cost=cost+1
    return init,cost+c
    


open=PriorityQueue()
close=[[]]
init=[2,0,3,1,8,4,7,6,5]
goal=[1,2,3,8,0,4,7,6,5]
close.append(init)
open.put((100,init))
c=0
print("Step",end=":")
print(c)
for i in range(9):
    if((i+1)%3!=0):
        print(init[i],end=" ")
    else:
        print(init[i])
        print()
print("---------------------------")
c=1
c1=1
while(init!=goal  or open.empty==True):
    print("Step",end=":")
    print(c)
    # print(init)
    # print("init")
    u,d,r,l=[],[],[],[]
    pos=init.index(0)
    if(pos!=2 and pos!=5 and pos!=8):
        r,rv=right(init.copy(),goal,pos,c1)
        # print(r)
        # print("right")
    if(pos!=0 and pos!=3and pos!=6):
        l,lv=left(init.copy(),goal,pos,c1)
        # print(l)
        # print("left")
    if(pos!=0 and pos!=1 and pos!=2):
        u,uv=up(init.copy(),goal,pos,c1)
        # print(u)
        # print("up")
    if(pos!=6 and pos!=7 and pos!=8):
        d,dv=down(init.copy(),goal,pos,c1)
        # print(d)
        # print("down")
    if r not in close:
        open.put((10-rv,r))
    if l not in close:
        open.put((10-lv,l))
    if u not in close:
        open.put((10-uv,u))
    if d not in close:
        open.put((10-dv,d))
    temp=open.get()[1]
    # print(list(temp))
    # print("temp")
    close.append(list(temp))
    # print(close)
    # print("close")
    # print(c)
    # print("step")
    # print(list(temp))
    init=list(temp)
    for i in range(9):
        if((i+1)%3!=0):
            print(init[i],end=" ")
        else:
            print(init[i])
            print()
    # print(init)
    print("---------------------------")
    c=c+1
    c1=c1+1
print("The end")
    