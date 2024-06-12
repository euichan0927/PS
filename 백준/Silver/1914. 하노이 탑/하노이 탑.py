import sys
input = sys.stdin.readline
n=int(input())

def hanoi(n,a,b,c):
    if n==1:
        print(a,c)
        return 0
    hanoi(n-1,a,c,b)
    print(a,c)
    hanoi(n-1,b,a,c)
print(2**n-1)
if n<=20:
    hanoi(n,1,2,3)