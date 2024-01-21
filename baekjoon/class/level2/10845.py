n=int(input())
result=[]
output=[]
for i in range(n):
    command=(input().split())
    if("push"in command):
        result.append(command[-1])
    elif("pop" in command):
        if(len(result)==0):
            output.append(-1)
        else:
            output.append(result[0])
            result.pop(0)
    elif("size" in command):
        output.append(len(result))
    elif("empty" in command):
        if(len(result)==0):
            output.append(1)
        else:
            output.append(0)
    elif("front" in command):
        if(len(result)==0):
            output.append(-1)
        else:
            output.append(result[0])
    elif("back" in command):
        if(len(result)==0):
            output.append(-1)
        else:
            output.append(result[-1])
for i in range(len(output)):
    print(output[i])