# 일반 queue를 사용해서 문제를 풀면 정답은 나오지만 시간초과.
## 여기서 시간을 더 아끼려면 어떻게 해야할까?
### 바로 collections 에 있는 deque 활용

#import sys
#input=sys.stdin.readline
#n=int(input())
#nlist=[]
#for i in range(n):
#    nlist.append(i+1)


#i=0

#while(len(nlist)>1):
#    nlist.pop(i)
#    num=nlist[0]
#    nlist.pop(i)
#    nlist.append(num)
#print(nlist[0])

from collections import deque
n=int(input())
deque = deque([i for i in range(1,n+1)])

while(len(deque)>1):
    deque.popleft()
    num=deque.popleft()
    deque.append(num)
print(deque[0])

