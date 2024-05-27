import sys
from collections import deque
input = sys.stdin.readline


def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    graph[x][y]=1
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if([nx,ny]==[en_x,en_y]):
                results.append(graph[x][y])
                return
            if(nx<0 or nx>=N or ny<0 or ny>=N):
                continue
            if(graph[nx][ny]!=0):
                continue
            if(graph[nx][ny]==0):
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))

dx=[-2,-1,-2,-1,2,1,2,1]
dy=[1,2,-1,-2,1,2,-1,-2]
T=int(input())
for i in range(T):
    results=[]
    N=int(input())
    graph=[[0]*(N) for _ in range(N)]
    st_x,st_y=map(int,input().split())
    en_x,en_y=map(int,input().split())
    if(st_x==en_x and st_y==en_y):
        print(0)
    else:
        bfs(st_x,st_y)
        print(min(results))