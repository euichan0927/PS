import sys
input=sys.stdin.readline
def 괄호():
    n=int(input())
    nlist=[]
    result=True
    nresult=[]
    for i in range(n):
        nlist=input()
        add=['']
        
        for j in range(len(nlist)-1):
            if(nlist[j]=='('):
                add.append(nlist[j])
            else:
                if(add[-1]=='('):
                    add.pop()
                else:
                    add.append(nlist[j])
                    result=False
                    
        if(len(add)==1):
            result=True
        else:
            result=False
        if(result==True):
            print('YES')
        else:
            print('NO')    
괄호()
