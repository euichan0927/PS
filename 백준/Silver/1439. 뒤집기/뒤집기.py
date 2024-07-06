import sys
input = sys.stdin.readline

s=list(input().rstrip())
count=0
for i in range(len(s)-1):
    if(s[i]!=s[i+1]):
        count+=1

else:
    print((count+1)//2)
