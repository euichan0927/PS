import sys
input = sys.stdin.readline

T=int(input())
nlist=[0]*(12)
nlist[1]=1
nlist[2]=2

if(T>2):
    nlist[3]=4
    for i in range(4,11):
        nlist[i]=nlist[i-1]+nlist[i-2]+nlist[i-3]
for i in range(T):
    num=int(input())
    print(nlist[num])


