n,m=map(int,input().split())

chess=[]
count=[]

for _ in range(n):
    chess.append(input())
    
for a in range(n-7):
    for b in range(m-7):
        cn = 0
        bn = 0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if((i+j)%2==0):
                    if(chess[i][j]!='W'):
                        cn+=1
                    if(chess[i][j]!='B'):
                        bn+=1
                else:
                    if(chess[i][j]!='B'):
                        cn+=1
                    if(chess[i][j]!='W'):
                        bn+=1
        count.append(min(cn,bn))
print(min(count))
    
    
