import sys,math
input=sys.stdin.readline


while(1):
    nlist=list(map(int,input().split()))
    nlist.sort()
    if(nlist[0]==0 and nlist[1]==0 and nlist[2]==0):
        break
    nmax=max(nlist)
    nlist.remove(nmax)

    if(nmax**2 == ((nlist[0]**2) + (nlist[1]**2))):
        print("right")
    else:
        print("wrong")
    