import sys
input = sys.stdin.readline

def gcd(a,b):
    if b == 0 :
        return a
    else:
        return gcd(b, a%b)

N, S = map(int, input().split())
A = list(map(int, input().split()))

distance = []
for i in A:
    distance.append(abs(i-S))

ans = distance[0]
for i in range(1,len(distance)):
    ans = gcd(ans, distance[i])
    
print(ans)