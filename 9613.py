import sys

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b, a%b)

n = int(input())
total = 0

for _ in range(n):
    li = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(li)):
        for j in range(i+1, len(li)):
            total += gcd(li[i], li[j])
    print(total)
    total = 0
            


        
        
        