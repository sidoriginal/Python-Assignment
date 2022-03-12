from queue import PriorityQueue
import queue

def right(init,goal,pos):
    temp=init[pos]
    init[pos]=init[pos+1]
    init[pos+1]=temp
    cost=0
    for i in range(9):
        if(init[i]!=goal[i]):
            cost=cost+1
    return init,cost


def left(init,goal,pos):
    temp=init[pos]
    init[pos]=init[pos-1]
    init[pos-1]=temp
    cost=0
    for i in range(9):
        if(init[i]!=goal[i]):
            cost=cost+1
    return init,cost


def up(init,goal,pos):
    temp=init[pos]
    init[pos]=init[pos-3]
    init[pos-3]=temp
    cost=0
    for i in range(9):
        if(init[i]!=goal[i]):
            cost=cost+1
    return init,cost


def down(init,goal,pos):
    temp=init[pos]
    init[pos]=init[pos+3]
    init[pos+3]=temp
    cost=0
    for i in range(9):
        if(init[i]!=goal[i]):
            cost=cost+1
    return init,cost
    


init=[2,8,3,1,5,4,7,6,0]
goal=[1,2,3,8,0,4,7,6,5]
c=0
min=0
# for i in range(9):
    # if(init[i]!=goal[i]):
    #     min=min+1
min=100
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
while(init!=goal):
    print("Step",end=":")
    print(c)
    temp=[]
    # print(init)
    # print("init")
    u,d,r,l=[],[],[],[]
    pos=init.index(0)
    if(pos!=2 and pos!=5 and pos!=8):
        r,rv=right(init.copy(),goal,pos)
        # print(rv)
        if(rv<=min):
            min=rv
            temp=r
        # print(min)
        # print(r)
        # print("right")
    if(pos!=0 and pos!=3and pos!=6):
        l,lv=left(init.copy(),goal,pos)
        # print(lv)
        if(lv<=min):
            min=lv
            temp=l
        # print(min)
        # print(l)
        # print("left")
    if(pos!=0 and pos!=1 and pos!=2):
        u,uv=up(init.copy(),goal,pos)
        # print(uv)
        if(uv<=min):
            min=uv
            temp=u
        # print(min)
        # print(u)
        # print("up")
    if(pos!=6 and pos!=7 and pos!=8):
        d,dv=down(init.copy(),goal,pos)
        # print(dv)
        if(dv<=min):
            min=dv
            temp=d
        # print(min)
        # print(d)
        # print("down")
    init=list(temp)
    
    if(init==[]):
        print("Cannot reach by hill climbing method")
        print("---------------------------")
        break
    for i in range(9):
        if((i+1)%3!=0):
            print(init[i],end=" ")
        else:
            print(init[i])
            print()
    print("---------------------------")
    c=c+1
print("The end")
    