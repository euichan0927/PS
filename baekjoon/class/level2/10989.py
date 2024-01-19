def sort3():
    import sys
    input=sys.stdin.readline
    n=int(input())
    nlist=[0]*100001
    for i in range(n):
        nlist[int(input())]+=1
    for i in range(len(nlist)):
        if(nlist[i]!=0):
            for _ in range(nlist[i]):
                print(i)
sort3()
