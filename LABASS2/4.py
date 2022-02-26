from re import S
from sys import maxsize
from itertools import permutations

def tsp(g,node,V):
    ver=[];
    for i in range (V):
        if(i!=node):
            ver.append(i);
    perm=permutations(ver)
    # for j in (perm):
    #     print(j)
    m=maxsize
    state=[]
    fin=[]
    for i in (perm):
        s=0
        ii=node
        for j in i:
            s=s+g[ii][j]
            ii=j
        s=s+g[ii][node]
        if(s<m):
            m=s
    print(m)


g=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
v=4
node=int(input("Enter the starting point "))
tsp(g,node-1,v)