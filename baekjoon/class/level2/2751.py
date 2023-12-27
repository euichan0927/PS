# input 시간단축으로 해결
# 파이썬은 병합 정렬과 삽입 정렬의 아이디어를 더한 하이브리드 방식의 정렬 알고리즘을 사용하고 있다.
import sys
input=sys.stdin.readline
a=int(input())
nlist=[]
for i in range(a):
    num=int(input())
    nlist.append(num)
nlist.sort()
for j in range(a):
    print(nlist[j])
