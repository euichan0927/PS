import sys
input = sys.stdin.readline

n=int(input())
nlist=[0]*1001

nlist[1]=1
nlist[2]=2
for i in range(3,1001):
    nlist[i]=(nlist[i-1]+nlist[i-2])%10007
print(nlist[n])
