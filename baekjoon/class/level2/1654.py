a,b=map(int,input().split())
list=[]
count=0

for i in range(a):
    num=int(input())
    list.append(num)

start=1
end=max(list)
while(start<=end):
    count_sum=0
    mid=(start+end)//2
    for i in range(a):
        count=list[i]//mid
        count_sum+=count
    
    if(count_sum<b):
        end=mid-1
    else:
        start=mid+1
    
print(end)
        
    
