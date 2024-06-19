import sys
from collections import deque
input = sys.stdin.readline
N=int(input())
graph=[]
result=[]
for i in range(N):
    nlist=list(map(int,input().rstrip()))
    graph.append(nlist)
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    global count
    count=1
    queue=deque()
    queue.append((x,y))
    graph[x][y]=0
    while queue:
        
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if(0<=nx<N and 0<=ny<N and graph[nx][ny]==1):
                count+=1
                graph[nx][ny]=0
                queue.append((nx,ny))
    return count

for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            result.append(bfs(i,j))
result.sort()
print(len(result))
for i in result:
    print(i)
