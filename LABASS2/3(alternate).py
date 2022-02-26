
def mvup(init,i,j):
	a = [row[:] for row in init]
	if(i>0):
		a[i][j],a[i-1][j]=a[i-1][j],a[i][j]
		return a	
	else:
		return a

def mvdown(init,i,j):
	a = [row[:] for row in init]
	if(i<2):
		a[i][j],a[i+1][j]=a[i+1][j],a[i][j]
		return a
	else:
		return a

def mvleft(init,i,j):
	a = [row[:] for row in init]
	if(j>0):
		a[i][j],a[i][j-1]=a[i][j-1],a[i][j]
		return a
	else:
		return a

def mvright(init,i,j):
	a = [row[:] for row in init]
	if(j<2):
		a[i][j],a[i][j+1]=a[i][j+1],a[i][j]
		return a
	else:
		return a

def fnl(init):
	for i in range(3):
		for j in range(3):
			if init[i][j]==0:
				return i,j
				

init=[[1,2,3],[8,0,4],[7,6,5]]
fin=[[2,8,1],[0,4,3],[7,6,5]]
q=[]
cl=[]
q.append(init)

while(not (len(q)==0)):

	curr=q.pop(0)
	cl.append(curr)
	print(curr)
	if(curr==fin):break
	i,j=fnl(curr)
	up=mvup(curr,i,j)
	if  not (up in cl):
		q.append(up)	
	right=mvright(curr,i,j)
	if(not(right in cl)):
		q.append(right)
	left=mvleft(curr,i,j)
	if(not(left in cl)):
		q.append(left)
	bottom=mvdown(curr,i,j)
	if(not(bottom in cl)):
		q.append(bottom)
	
	
	
    
