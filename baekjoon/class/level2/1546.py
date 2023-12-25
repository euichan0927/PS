a=int(input())
sum=0
list=list(map(int,input().split()))
max=max(list)

for i in range(a):
    list[i]=(list[i]/max)*100
    sum+=list[i]
print(sum/a)

