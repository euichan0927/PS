import sys
input= sys.stdin.readline
n=int(input())
time=[0]*(n+1)
cost=[0]*(n+1)
sum=[]
dp=[0]*(n+3)
for i in range(1,n+1):
    a,b=map(int,input().split())
    time[i]=a
    cost[i]=b
for i in range(n,0,-1):
    if(i+time[i]>n+1):
        dp[i]=dp[i+1]
    else:
        dp[i]=max(dp[i+1],dp[i+time[i]]+cost[i])
print(dp[1])

