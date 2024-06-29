import sys
input = sys.stdin.readline
n=int(input())

nlist=list(map(int,input().split()))

for i in range(1,n):
    nlist[i]=max(nlist[i],nlist[i]+nlist[i-1])
        
print(max(nlist))