import sys
input = sys.stdin.readline
from collections import deque
def bfs():
    queue=deque()
    queue.append(N)
    while queue:
        x=queue.popleft()
        if(x==K):
            print(dist[x])
            break
        for nx in (x-1,x+1,x*2):
            if 0 <= nx <=MAX and dist[nx]==0:
                dist[nx] = dist[x]+1
                queue.append(nx)

N,K=map(int,input().split())
MAX=10**5
dist= [0]*(MAX +1)
bfs()
