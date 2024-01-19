def 이항계수():
    import sys
    input=sys.stdin.readline
    n,k=map(int,input().split())
    sum=1
    sum2=1
    for i in range(1,k+1):
        sum*=n
        n-=1
        sum2*=i

    print(sum//sum2)
이항계수()