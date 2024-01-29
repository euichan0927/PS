import sys
input=sys.stdin.readline
n=int(input())
sum=0
nlist=list(map(int,input().split()))
nlist.sort()
for i in range(n):
    for j in range(0,n-i):
        sum+=nlist[j]
print(sum)