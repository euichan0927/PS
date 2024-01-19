import sys
input = sys.stdin.readline
nlist=[]
n=int(input())

for i in range(n):
    [a,b]=map(int,input().split())
    nlist.append([a,b])

nlist=sorted(nlist)

for i in range(n):
    print(nlist[i][0],nlist[i][1])