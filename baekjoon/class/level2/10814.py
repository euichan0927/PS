n=int(input())
nlist=[]
for i in range(n):
    age,name=(input().split())
    nlist.append((int(age),name))
sort_list=sorted(nlist,key=lambda x:x[0])
for i in range(n):
    print(sort_list[i][0] , sort_list[i][1])
