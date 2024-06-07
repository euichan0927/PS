import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
N,M,R=map(int,input().split())
graph=[[] for _ in range(N+1)]
visited=[0]*(N+1)
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()


count=1
def dfs(R):
    global count
    visited[R]=count
    for x in graph[R]:
        if(visited[x]==0):
            count+=1
            dfs(x)
visited[R]=count
dfs(R)

for i in range(1,N+1):
    print(visited[i])