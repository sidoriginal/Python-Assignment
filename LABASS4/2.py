import copy



def heuri(block,goal):
    istate=0
    for j in block:
        if j==[0]:
            continue
        cp=1
        for i in range (1,len(j)):
            if(cp==-1):
                st=-1*(i-1)
                istate=istate+st
                # print('for',j[i],'istate=',istate,'st=',st)
                continue
            if(j[i]==goal[i]):
                st=1*(i-1)
                istate=istate+st
                # print('for',j[i],'istate=',istate,'st=',st)
            else:
                cp=-1
                st=-1*(i-1)
                istate=istate+st
                # print('for',j[i],'istate=',istate,'st=',st)
    return istate
    
    






def fun(block,goal,istate):
    tist=-1000
    tt=[[]]
    for j in block:
        if(j==[0] or j==[]):
            continue
        temp=copy.deepcopy(block)
        # print(block,temp)
        ind=block.index(j)
        # print(j)
        # print(temp)
        # print(temp)
        # print(j)
        for k in temp:
            # print(k)
            if(k==j):
                # print(k)
                bl=k[len(k)-1]

                k.remove(bl)
                
        for i in temp:
            # print(i)
            if(i==[]):
                continue
            if(i==j):
                # print(i)
                # bl=i[len(i)-1]
                # i.remove(bl)
                continue
            # print(i)
            i.append(bl)
            tis=heuri(temp.copy(),goal)
            # print(temp,tis)
            if(tis>tist):
                # print(tis)
                # print(temp)
                tist=tis
                tt=copy.deepcopy(temp)
                # print(tt)
            # print('here',tt)
            i.remove(bl)
            # print('here1',tt)
    # print('hh',tt)
    return tt,tist
                
            
        

        
        

    
def disp(block,h):
    for j in block:
        if(j==[0]):
            continue
        for i in j:
            if(i==0):
                continue
            print(i,end=' | ')
        print()
    print()
    print('heuristic for this=',h)
    print('______________________________________')
             
    
         
        


initial=[[0,2,3,4,1],[0],[0],[0]]
goal=[0,1,2,3,4]
block=[]
block=initial.copy()
gc=[goal,[],[]]
gstate=heuri(gc,goal)
istate=heuri(block,goal)
            # c=-1
        # print(c,'after ',i,'ist=',istate)
# print(istate)
# disp(block,istate)
# print(block)
while(gstate!=istate):
    disp(block,istate)
    temp=-1
    tempi=copy.deepcopy(block)
    tempg=goal.copy()
    res,val=fun(tempi,tempg,istate);
    # print(val)
    # print(res)
    if(val<=istate):
        print('Cant climb the hill beacuse heuristics are low now')
        break
    else:
        istate=val
        block=res
if(gstate==istate):
    disp(block,istate)
    print('The end')
    
    
    
    
        
        
        
     
        
        
    


