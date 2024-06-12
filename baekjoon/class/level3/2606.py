import sys
input = sys.stdin.readline

n=int(input())
m=int(input())


graph=[[] for _ in range(n+1)]
visit=[0]*(n+1)

for i in range(m):
    key,value=map(int,input().split())
    graph[key]+=[value]
    graph[value]+=[key]

def dfs(n):
    visit[n]=1
    for i in graph[n]:
        if(visit[i]==0):
            dfs(i)
dfs(1)
print(sum(visit)-1)
print(graph)