
from collections import Counter
n=int(input())
nlist=list(map(int,input().split()))
m=int(input())
mlist=list(map(int,input().split()))

nlist.sort()
c=Counter(nlist)
for i in range(m):
    if(mlist[i] in c):
        print(c[mlist[i]], end=' ')
    else:
        print(0,end=' ')
