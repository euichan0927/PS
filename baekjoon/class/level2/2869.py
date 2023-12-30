import sys
import math
input=sys.stdin.readline
a,b,v,=map(int,input().split())
print(int(math.ceil((v-b)/(a-b))))

