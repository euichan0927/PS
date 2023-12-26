a=int(input())
result=1
count=0
for i in range(1,a+1):
    result=result*i
list=list(map(int,str(result)))

for i in range(len(list)-1,0,-1):
    
    if(list[i]==0):
        count+=1
    else:
        break
print(count)
    


// int 형으로 받은 a 값의 각 한자리씩의 숫자를 확인하기 위해서 list로 변환해야했다.
단순히 list() 로 하면 불가능하고, list(map(int,str(n))) 형태를 사용해야함.
