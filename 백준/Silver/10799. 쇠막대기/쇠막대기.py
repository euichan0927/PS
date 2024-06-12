import sys
input = sys.stdin.readline
nlist=[]
add=[]
count=0
nlist=input()
for i in range(len(nlist)-1):
    if(nlist[i]=='('):
        add.append(nlist[i])
    else:
        if(nlist[i-1]=='('):
            add.pop(-1)
            count+=len(add)
        else:
            add.pop(-1)
            count+=1

print(count)