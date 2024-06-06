import sys
from collections import deque
input=sys.stdin.readline

N,M,R = map(int,input().split())
graph=[[] for _ in range(N+1)]
visited=[-1]*(N+1)
for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

depth=[-1]*(N+1)
def bfs():
    queue=deque()
    queue.append(R)
    visited[R]=0
    depth[R]=0
    num=2
    while queue:
        x=queue.popleft()
        for i in graph[x]:
            if visited[i]==-1:
                queue.append(i)
                visited[i]=(depth[x]+1)*num
                depth[i]=depth[x]+1
                num+=1
            
        

bfs()

sum=0
for i in range(1,N+1):
    if(visited[i]==-1):
        visited[i]=0
    sum+=visited[i]
print(sum)