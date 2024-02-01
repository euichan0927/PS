def solution(s):
    result=list()
    for i in range(len(s)):
        if(s[i]=='('):
            result.append('(')
        else:
            if(len(result)==0):
                return False
            else:
                if(result[-1]=='('):
                    result.pop(-1)
                
    if(len(result)==0):
        return True
    else:
        return False
    