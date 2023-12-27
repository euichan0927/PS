import sys
input=sys.stdin.readline
n,m=map(int,input().split())

nlist=list(map(int,input().split()))
sum=[]

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            max1=nlist[i]+nlist[j]+nlist[k]
            if(max1<=m):
                sum.append(max1)
                

print(max(sum))
