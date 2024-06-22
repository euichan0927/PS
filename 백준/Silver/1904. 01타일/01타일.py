import sys
input = sys.stdin.readline

N=int(input())

nlist=[0]*(N+1)
nlist[1]=1
if(N>1):
    nlist[2]=2
if N>=3:
    for i in range(3,N+1):
        nlist[i]=(nlist[i-1]+nlist[i-2])%15746
print(nlist[N])