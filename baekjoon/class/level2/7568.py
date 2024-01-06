def 덩치():
    n=int(input())
    nlist=[]

    for _ in range(n):
        a,b=map(int,input().split())
        nlist.append((a,b))


    for i in range(n):
        rank=1
        for j in range(n): 
            if(nlist[i][0]<nlist[j][0] and nlist[i][1]<nlist[j][1]):
                rank+=1
        print(rank)

덩치()
