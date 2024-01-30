import sys
input = sys.stdin.readline
all_set=set([str(i) for i in range(1,21)])
nlist=set()
m=int(input())
for i in range(m):
    command=(input().split())
    if("add" in command):
        nlist.add(command[1])
    elif("remove" in command):
        nlist.discard(command[1])
    elif("check" in command):
        if(command[1] in nlist):
            print(1)
        else:
            print(0)
    elif("toggle" in command):
        if(command[1] in nlist):
            nlist.discard(command[1])
        else:
            nlist.add(command[1])
    elif("all" in command):
        nlist=all_set.copy()
        
    elif("empty" in command):
        nlist=set()
        