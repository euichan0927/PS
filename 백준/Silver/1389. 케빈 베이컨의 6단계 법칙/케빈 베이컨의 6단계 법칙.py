import sys
input = sys.stdin.readline
from collections import deque

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]

result=[0]*(N+1)
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(R):
    visited=[0]*(N+1)
    queue=deque()
    queue.append(R)
    while queue:
        x=queue.popleft()
        for y in graph[x]:
            if(visited[y]==0):
                visited[y]=visited[x]+1
                queue.append(y)
    result[R]=sum(visited)

bfs(1)
min=result[1]

for i in range(1,N+1):
    bfs(i)
    if(result[i]<min):
        min=result[i]
for i in range(1,N+1):
    if(min==result[i]):
        print(i)
        break
    

