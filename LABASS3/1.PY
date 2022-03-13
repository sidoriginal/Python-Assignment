from math import sqrt
def mhd(g,i):
    if(g==0 or g==1 or g==2):
        xg=g
        yg=0
    if(g==3 or g==4 or g==5):
        xg=g-3
        yg=1
    if(g==6 or g==7 or g==8):
        xg=g-6
        yg=2
    if(i==0 or i==1 or i==2):
        xi=i
        yi=0
    if(i==3 or i==4 or i==5):
        xi=i-3
        yi=1
    if(i==6 or i==7 or i==8):
        xi=i-6
        yi=2
    return abs(xi-xg)+abs(yi-yg)

def eu(g,i):
    if(g==0 or g==1 or g==2):
        xg=g
        yg=0
    if(g==3 or g==4 or g==5):
        xg=g-3
        yg=1
    if(g==6 or g==7 or g==8):
        xg=g-6
        yg=2
    if(i==0 or i==1 or i==2):
        xi=i
        yi=0
    if(i==3 or i==4 or i==5):
        xi=i-3
        yi=1
    if(i==6 or i==7 or i==8):
        xi=i-6
        yi=2
    return sqrt(pow((xi-xg),2)+pow((yi-yg),2))

def mink(g,i,p):
    if(g==0 or g==1 or g==2):
        xg=g
        yg=0
    if(g==3 or g==4 or g==5):
        xg=g-3
        yg=1
    if(g==6 or g==7 or g==8):
        xg=g-6
        yg=2
    if(i==0 or i==1 or i==2):
        xi=i
        yi=0
    if(i==3 or i==4 or i==5):
        xi=i-3
        yi=1
    if(i==6 or i==7 or i==8):
        xi=i-6
        yi=2
    return pow(pow(abs(xi-xg),p)+pow(abs(yi-yg),p),1/p)
    
    


init=[2,0,3,1,8,4,7,6,5]
goal=[1,2,3,8,0,4,7,6,5]
sum=0
sum1=0
sum2=0
sum3=0
sum4=0
for i in range(9):
    if(i==0):
        continue
    g=goal.index(i)
    i=init.index(i)
    sum=sum+mhd(g,i)
    sum1=sum1+eu(g,i)
    sum2=sum2+mink(g,i,1)
    sum3=sum3+mink(g,i,2)
    sum4=sum4+mink(g,i,5)
print("Manhattan = ",sum)
print("Eucledian =",sum1)
print("Minkowski for p=1(Manhattan) =",sum2)
print("Minkowski for p=2(Eucledian) =",sum3)
print("Minkowski for p=5 =",sum4)


