import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N,M,R=map(int,input().split())
graph=[[] for _ in range(N+1)]
visited=[-1]*(N+1)
result=[0]*(N+1)
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(N+1):
    graph[i].sort(reverse=True)

def dfs(R):
    global count
    for x in graph[R]:
        if(visited[x]==-1):
            count+=1
            visited[x]=visited[R]+1
            result[x]=visited[x]*count
            dfs(x)
count=1
visited[R]=0
dfs(R)
print(sum(result))