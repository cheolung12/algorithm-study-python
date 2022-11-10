import sys
input = sys.stdin.readline

n, k = map(int, input().split())
circle = [i+1 for i in range(n)]
result = []
num = 0

for _ in range(n):
    num += k-1  
    if num >= len(circle):   
        num = num % len(circle)
    result.append(str(circle.pop(num)))

    
print("<" + ', '.join(result) + ">")       
    


