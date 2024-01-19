import sys
input = sys.stdin.readline
nlist=[]
n=int(input())

for i in range(n):
    [a,b]=map(int,input().split())
    nlist.append([a,b])

nlist=sorted(nlist)
nlist=sorted(nlist,key=lambda x:x[1])

# for i in range(n-1):
#     if(nlist[i][0]>nlist[i+1][0]):
#         nlist[i][0] , nlist[i+1][0] = nlist[i+1][0] , nlist[i][0]

for i in range(n):
    print(nlist[i][0],nlist[i][1])