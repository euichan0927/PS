import sys
input = sys.stdin.readline
n=int(input())
dp=[0]*301
s=[0]*301
for i in range(1,n+1):
    s[i]=int(input())
dp[1]=s[1]
dp[2]=s[1]+s[2]
dp[3]=max(s[1]+s[3],s[2]+s[3])
for i in range(4,n+1):
    dp[i]=max(dp[i-3]+s[i-1]+s[i],dp[i-2]+s[i])
if(n==1):
    print(dp[1])
elif(n==2):
    print(dp[2])
elif(n==3):
    print(dp[3])
else:
    print(dp[n])