a=int(input())


result=False
for i in range(1,a+1):
    sum=0
    a_list=list(map(int,str(i)))
    
    for j in range(len(a_list)):
        sum+=a_list[j]

    if((sum+i)==a):
        result=True
        print(i)
        break
if(result==False):
    print(0)
