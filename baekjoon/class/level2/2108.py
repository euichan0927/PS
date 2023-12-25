# 리스트 빈도수 세기
## collections 에서 Counter 함수
### 튜플 형식의 결과
import sys
input=sys.stdin.readline
# 평소에 사용하던 input은 시간이 오래 걸리지만 이렇게 사용하면 시간을 절약할 수 있음.
# 이걸 쓰지 않았을땐 시간초과 , 사용한 후 성공
# 앞으로 평소에 먼저 기입하고 사용할 것 !
import collections

a=int(input())
nlist=[]
sum=0
for _ in range(a):
    num=int(input())
    nlist.append(num)
    sum+=num

nlist.sort()

counts=collections.Counter(nlist)


avg=sum/a
center= nlist[a//2]
highfre=counts.most_common()[0][0]
if(a>2):
    high=counts.most_common()[0][1]
    second=counts.most_common()[1][1]
    if(high==second):
        highfre=counts.most_common()[1][0]
        
end=nlist[-1]-nlist[0]
print(round(avg))
print(center)
print(highfre)
print(end)
