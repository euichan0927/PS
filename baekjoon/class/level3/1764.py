import sys
inpuy = sys.stdin.readline
nlist=set()
mlist=set()
result=[]
n,m = map(int,input().split())
for i in range(n):
    name=input()
    nlist.add(name)
for j in range(m):
    name=input()
    mlist.add(name)

result=list(nlist.intersection(mlist))
result.sort()
print(len(result))
for i in result:
    print(i)
