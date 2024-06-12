import sys
from collections import deque
input = sys.stdin.readline
N,M,R=map(int,input().split())
graph=[[] for _ in range(N+1)]
for i in range(N+1):
    graph[i].sort()

visited=[-1]*(N+1)
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    queue=deque()
    queue.append(R)
    visited[R]=0
    count=1
    while queue:
        x=queue.popleft()
        for i in graph[x]:
            if visited[i]==-1:
                queue.append(i)
                visited[i]=visited[x]+1
        
bfs()
for i in range(1,N+1):
    print(visited[i])