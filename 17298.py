import sys

N = int(input())
L = list(map(int,sys.stdin.readline().split()))

stack = []
A = [-1]*N
print(A)

for i in range(N-1,-1,-1):
    
    while stack:
        if stack[-1] > L[i]:
            A[i] = stack[-1]
            break
        else:
            stack.pop()
    stack.append(L[i])    

print(" ".join(map(str,A)))

            
    








    
