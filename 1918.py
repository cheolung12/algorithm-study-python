import sys

data = sys.stdin.readline().rstrip()
stack = []
result = ""

for i in data:
    if('A' <= i <= 'Z'):
        result += i
    else:
        if(i == '('):
            stack.append(i)
        elif(i==')'):
            while(stack and stack[-1] != '('):
                result += stack.pop()
            stack.pop() # '(' 수거
        elif(i == '*' or i == '/'):
            while(stack and stack[-1] != '(' and (stack[-1] == '*' or stack[-1] == '/')):
                    result += stack.pop()
            stack.append(i)
        elif(i == '+' or i == '-'):
            while(stack and stack[-1] != '('):
                result += stack.pop()
            stack.append(i)
     
while(stack):
    result += stack.pop()

print(result)