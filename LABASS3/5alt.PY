from queue import PriorityQueue
def ucs(start,goal,v,cost):
    visited=[]
    path=[]
    bt=[]
    deal=-1
    sum=0
    visited.append(start)
    bts=[]
    while(deal!=goal):
        min=1000
        temp=-1
        # print(visited)
        path.append(start)
        for i in range(0,v):
            # print(i)
            if(cost[start][i]!=-1 and cost[start][i]!=0 and i not in visited):
                
                if(cost[start][i]<min):
                    min=cost[start][i]
                    temp=i
        if(temp==-1):
            # print(prob)
            visited.append(start)
            sum=sum+bts[len(bts)-1]
            bts.pop(len(bts)-1)
            start=bt[len(bt)-1]
            bt.pop(len(bt)-1)
            visited.remove(start)
        else:
            bts.append(min)
            bt.append(start)
            start=temp
            visited.append(start)
            sum=sum+min
            deal=temp
        # print(temp)
        # print(start)
        # print(sum)
            
    path.append(goal)
    print(sum)
    print(path)
        
                
    
    




cost=[[0,1,-1,10,-1],[1,0,5,-1,15],[-1,5,0,5,-1],[10,-1,5,0,5],[-1,15,-1,5,0]]
V=5
# cost=[[0,1,-1,-1,-1,-1],[1,0,2,7,-1,-1],[-1,2,0,-1,3,-1],[-1,7,-1,0,-1,-1],[-1,-1,3,-1,0,4],[-1,-1,-1,-1,4,0]]
# V=6
# print(graph)
# print(cost)
start= 0
goal = 3
ucs(start,goal,V,cost)
