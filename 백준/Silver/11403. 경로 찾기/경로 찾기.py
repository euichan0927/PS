import sys
from collections import deque
input = sys.stdin.readline


N=int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
result=[[0]*N for _ in range(N)]


def bfs(R):
    queue=deque()
    queue.append(R)
    visited=[0 for _ in range(N)]
    while queue:
        x=queue.popleft()
        for i in range(N):
            if(graph[x][i]==1 and visited[i]==0):
                queue.append(i)
                visited[i]=1
                result[R][i]=1
for i in range(0,N):
    bfs(i)
for i in result:
    print(*i)

