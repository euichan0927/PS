import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
def dfs(a,b):
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    for i in range(4):
        nx=a+dx[i]
        ny=b+dy[i]
        if(0<=nx<M) and (0<=ny<N) :
            if(graph[nx][ny]==1):
                graph[nx][ny]=0
                dfs(nx,ny)

T=int(input())
for i in range(T):
    M,N,K=map(int,input().split())
    graph=[[0 for _ in range(N)] for _ in range(M)]
    count=0
    for i in range(K):
        a,b=map(int,input().split())
        graph[a][b]=1
    
    for k in range(M):
        for j in range(N):
            if graph[k][j]==1:
                dfs(k,j)
                count+=1
    print(count)
    
