import sys
input = sys.stdin.readline
nlist=[]
n,k=map(int,input().split())
for i in range(n):
    num=int(input())
    nlist.append(num)
sum=0
count=0
nlist.sort(reverse=True)
i=0
while(sum<k):
    if(((k-sum)//nlist[i])>=1):
        count+=((k-sum)//nlist[i])
        sum+=((k-sum)//nlist[i])*nlist[i]
    i+=1
print(count)
