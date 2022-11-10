import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

dict = {}
answer = [-1] * n

for i in data:
    if(dict.get(i)):
        dict[i] += 1
    else:
        dict[i] = 1


stack = []
for i in range(n):
    while stack and dict.get(data[stack[-1]]) < dict.get(data[i]):
        answer[stack.pop()] = data[i]
        print(answer)
    stack.append(i)

print(*answer)
