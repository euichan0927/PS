import sys
input=sys.stdin.readline
t=int(input())
nlist=[]
for i in range(t):
    nlist=[]
    k=int(input())
    n=int(input())
    for a in range(1,n+1):
        nlist.append(a)

    for x in range(k):
        for y in range(1,n):
            nlist[y]+=nlist[y-1]
    print(nlist[-1])
