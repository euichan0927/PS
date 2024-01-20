import sys
import math
input=sys.stdin.readline
n=int(input())
nlist=[]
if(n==0):
    print(0)
else:
    for i in range(n):
        a=int(input())
        nlist.append(a)

    if(n==0):
        print(0)

    nlist.sort()
    div=n*0.15
    div=math.floor(div+0.5)

    sum=0
    for i in range(div,n-div):
        sum+=nlist[i]

    print(math.floor((sum/(n-(2*div)))+0.5))