# 에라토스테네스의 체 알고리즘 (소수 구하기)
## 기존 소수 구하는 알고리즘은 2부터 주어진 수 끝까지 나누어보고 나눠 떨어지는 수가 자기 자신이 아닌 다른 수가 있다면 소수가 아닌 알고리즘인데
## 이것은 하나씩 끝까지 탐색하기 때문에 시간에 대한 비효율성을 야기함.

### 따라서 에라토스테네스의 체 알고리즘 사용
### -> 특정 수 N이 소수인지 확인하려면 2부터 N의 제곱근까지의 수로 나누어보면 알 수 있다.
### -> 2부터 N의 제곱근 까지 나누었을 때 나누어 떨어진다면 소수가 아니고, 나누어 떨어지지 않는다면 소수이다.

a,b=map(int,input().split())

def is_prime_number(num):
    if(num==1):
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if((num%i) ==0):
                return False
        return True
for i in range(a,b+1):
    if is_prime_number(i):
        print(i)
                
            
