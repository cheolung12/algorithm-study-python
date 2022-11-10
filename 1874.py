import sys
input = sys.stdin.readline

n = int(input())

cnt = 1
stack = []
result = []

for _ in range(n):
    data = int(input())

    # 1~입력값까지 오름차순 수열 만들기 **
    while( cnt <= data):  
        stack.append(cnt)
        cnt += 1
        result.append('+')
    
    # 같으면 뺀다
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)
        
print('\n'.join(result))




'''
input = sys.stdin.readline
선언 후 input() 하는 방식도 있음(가독성 향상.?)
'''