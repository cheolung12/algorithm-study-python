import math

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    x = math.gcd(n,m)
    print(math.trunc(x * (n/x) * (m/x)))

# math.lcm 이라는 함수도 있었네...
