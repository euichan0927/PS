import sys
input = sys.stdin.readline
from collections import deque
F,S,G,U,D=map(int,input().split())
graph=[]*(F+1)
visited=[0]*(F+1)
result=[]

def bfs(S):
    
    queue=deque()
    queue.append(S)
    visited[S]=1
    while queue:
        x=queue.popleft()
        
        for nx in (x+U,x-D):
            if(0<nx<=F and visited[nx]==0):
                
                visited[nx]=visited[x]+1
                if(nx==G):
                    result.append(visited[nx]-1)
                else:
                    
                    queue.append(nx)
bfs(S)
if(S==G):
    print(0)
else:
    if(result):
        print(min(result))
    else:
        print('use the stairs')

            

                
