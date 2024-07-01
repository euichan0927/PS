import sys
input = sys.stdin.readline
n=int(input())

nlist=list(map(int,input().split()))
dp=[1]*n
dp[0]=nlist[0]
for i in range(n):
    for j in range(i):
        if(nlist[i]>nlist[j]):
            dp[i]=max(dp[i],nlist[i]+dp[j])
        else:
            dp[i]=max(dp[i],nlist[i])
                    
print(max(dp))