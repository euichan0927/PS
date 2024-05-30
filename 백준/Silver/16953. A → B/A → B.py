import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**9)
count=0

def bfs(count):
  queue=deque()
  queue.append((A,count))
  
  while queue:
    x,count=queue.popleft()
    if(x==B):
        return count+1
        break
    for nx in (x*2,(x*10)+1):
      if(1<=nx<=10**9):
        queue.append((nx,count+1))
  return -1   

      
A,B=map(int,input().split())
print(bfs(count))
