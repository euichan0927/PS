# 최대공약수 , 최소공배수 문제
# math 라이브러리에서 gcd (최대공약수) lcm(최소공배수) 함수 사용

import math
import sys
input=sys.stdin.readline
a,b=map(int,input().split())
min=math.gcd(a,b)
max=math.lcm(a,b)
print(min)
print(max)
