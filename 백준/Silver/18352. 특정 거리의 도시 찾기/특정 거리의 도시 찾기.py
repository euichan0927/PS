import sys
input = sys.stdin.readline
from collections import deque

N,M,K,X=map(int,input().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    A,B=map(int,input().split())
    graph[A].append(B)
    

count=[0]*(N+1)
visited=[0]*(N+1)
answer=[]
def bfs():
    queue=deque()
    queue.append(X)
    while queue:
        x=queue.popleft()
        visited[x]=1
        for i in graph[x]:
            if(visited[i]==0):
                queue.append(i)
                visited[i]=1
                count[i]=count[x]+1
                if(count[i]==K):
                    answer.append(i)

    if(answer):
        answer.sort()
        for i in range(len(answer)):
            print(answer[i])
    else:
        print(-1)
bfs()