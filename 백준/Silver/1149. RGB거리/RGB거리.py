import sys
input = sys.stdin.readline
n=int(input())
nlist=[]
for i in range(n):
    rgb=list(map(int,input().split()))
    nlist.append(rgb)
for i in range(1,n):
    nlist[i][0]=min(nlist[i-1][1],nlist[i-1][2]) + nlist[i][0]
    nlist[i][1]=min(nlist[i-1][0],nlist[i-1][2]) + nlist[i][1]
    nlist[i][2]=min(nlist[i-1][0],nlist[i-1][1]) + nlist[i][2]
print(min(nlist[n-1][0],nlist[n-1][1],nlist[n-1][2]))
    

