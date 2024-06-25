import sys
input = sys.stdin.readline
T=int(input())

P=[0]*(101)
def func(num):
    P[1]=1
    P[2]=1
    P[3]=1
    if(num>3):
        for i in range(4,num+1):
            P[i]=P[i-2]+P[i-3]

for i in range(T):
    num=int(input())
    func(num)
    print(P[num])