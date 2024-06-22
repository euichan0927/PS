import sys
input = sys.stdin.readline
N=int(input())

stone=N
i=0
dx=[1,3]
if(stone%2==0):
    print('CY')
else:
    print('SK')
