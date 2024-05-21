import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

N,M=map(int,input().split())
graph=[[0]*(N+1) for _ in range(N+1)]
visited=[0]*(N+1)
count=0

for i in range(M):
    a,b=map(int,input().split())
    if(i==0):
        num=a
    graph[a][b]=graph[b][a]=1


def dfs(num):
    visited[num]=1
    for i in range(1,N+1):
        if(graph[num][i]==1 and visited[i]==0):
            dfs(i)
            
for i in range(1,N+1):
    if visited[i]==0:
        dfs(i)
        count+=1

print(count)


     