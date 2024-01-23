# import sys
# input=sys.stdin.readline
# n=int(input())
# num1=0
# num2=0
# nlist1=[]
# nlist2=[]
# def fibonacci(n):
#     global num1,num2
#     if(n==0):
#         num1+=1
#         return 0
#     elif(n==1):
#         num2+=1
#         return 1
        
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# for i in range(n):
#     num1=0
#     num2=0
#     a=int(input())
#     fibonacci(a)
#     nlist1.append(num1)
#     nlist2.append(num2)
# for i in range(n):
#     print(nlist1[i],nlist2[i])

import sys
input=sys.stdin.readline
n=int(input())
nlist1=[]
nlist2=[]
for _ in range(n):
    a=int(input())
    num1=1
    num2=0
    for i in range(a):
        num1 , num2 = num2, num1+num2
    nlist1.append(num1)
    nlist2.append(num2)
for i in range(n):
    print(nlist1[i],nlist2[i])