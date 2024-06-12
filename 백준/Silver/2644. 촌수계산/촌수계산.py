import sys
input = sys.stdin.readline
n=int(input())
x,y=map(int,input().split())
m=int(input())
count=0
graph=[[0]*(n+1) for _ in range(n+1)]
visited=[0]*(n+1)

for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=graph[b][a]=1

def dfs(x,y,count):
    global flag
    visited[x]=1
    if(x==y):
        flag=True
        print(count)
    for i in range(1,n+1):
        if(graph[x][i]==1 and visited[i]==0):
            dfs(i,y,count+1)
flag=False
dfs(x,y,0)
if(flag==False):
    print(-1)