import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
result = deque()

for i in range(n):
    command = input().split()
    if(command[0] == 'push_front'):
        result.appendleft(command[1])
    elif(command[0] == 'push_back'):
        result.append(command[1])
    elif(command[0] == 'pop_front'):
        try:
            print(result.popleft())
        except:
            print(-1)
    elif(command[0] == 'pop_back'):
        try:
            print(result.pop())
        except:
            print(-1)
    elif(command[0] == 'size'):
        print(len(result))
    elif(command[0] == 'empty'):
        if(len(result)==0):
            print(1)
        else:
            print(0)
    elif(command[0] == 'front'):
        try:
            print(result[0])
        except:
            print(-1)
    elif(command[0] == 'back'):
        try:
            print(result[-1])
        except:
            print(-1)


