## queue 문제
### FIFO 구조

num=int(input())
for _ in range(num):
    a,b=map(int,input().split())

    mylist=list(map(int,input().split()))
    i=0
    count=0
    find=b

    while(len(mylist)>0):
        
        if(mylist[i]==max(mylist)):
            if(i==find):
                count+=1
                break
            mylist.pop(i)
            count+=1
            find=find-1
            
        else:
            
            if(i==find):
                popnum=mylist.pop(i)
                mylist.append(popnum)
                find+=(len(mylist)-1)
                
            else:
                popnum=mylist.pop(i)
                mylist.append(popnum)
                find-=1
    
    print(count)
        


    
