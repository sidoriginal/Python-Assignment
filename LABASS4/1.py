import copy



def heuri(block,goal):
    istate=0
    for j in block:
        for i in range (1,5):
            if(i not in j):
                continue
            indg=goal.index(i)
            indb=j.index(i)
            if(j[indb-1]==goal[indg-1]):
                # c=1
                istate=istate+1
                # print(c,'after ',i,'ist=',istate)
            else:
                istate=istate-1
                # c=-1
                # print(c,'after ',i,'ist=',istate)
    return istate
    
    






def fun(block,goal,istate):
    tist=-1000
    tt=[[]]
    for j in block:
        if(j==[0]):
            continue
        temp=block.copy()
        ind=block.index(j)
        # print(temp)
        for i in temp:
            # print(i)
            if(i==[]):
                continue
            if(ind==temp.index(i)):
                # print(i)
                bl=i[len(i)-1]
                i.remove(bl)
                continue
            i.append(bl)
            # print(temp)
            tis=heuri(temp.copy(),goal)
            if(tis>tist):
                # print(tis)
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
gstate=4
istate=heuri(block,goal)
            # c=-1
        # print(c,'after ',i,'ist=',istate)
# print(istate)
# disp(block,istate)
# print(block)
while(gstate!=istate):
    disp(block,istate)
    temp=-1
    tempi=block.copy()
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
    
    
    
        
        
        
     
        
        
    


