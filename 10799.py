import sys
input = sys.stdin.readline

bar_lazor = input().rstrip()
stack = []
result = 0

for i in range(len(bar_lazor)):
    if(bar_lazor[i] == '('):
        stack.append('(')
    else:  # ')' 일 때
        if (bar_lazor[i-1] == '('):
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1

print(result)
            
            
            
            

        




