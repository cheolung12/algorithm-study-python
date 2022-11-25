import math
num1, num2 =  map(int, input().split())

if(num1 < num2):
    temp = num1
    num1 = num2
    num2 = temp

def gcd(num1, num2):
    if(num2 == 0):
        return num1
    else:
        return gcd(num2, num1%num2)

x = gcd(num1, num2)
print(x)
print(math.trunc(x * (num1/x) * (num2/x)))

# 놀라운건 math.gcd 함수가 있었다는거 ^^


        
