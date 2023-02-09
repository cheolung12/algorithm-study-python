import sys
n = int(sys.stdin.readline())
data = sys.stdin.readline().rstrip()
operand = [0] * n     # 피연산자를 저장할 스택
stack = []         # 연산자를 저장할 스택

for i in range(n):
    operand[i] = int(sys.stdin.readline())    # 피연산자값을 받는다

for i in data:
    if('A' <= i <= 'Z'):    # 후위표기식에서 알파벳을 만나면
        stack.append(operand[ord(i)-ord('A')])
    else:                   # 연산자를 만나면
        str2 = stack.pop()
        str1 = stack.pop()
        
        if(i == '+'):
            stack.append(str1+str2)
        elif(i == '-'):
            stack.append(str1-str2)
        elif(i == '*'):
            stack.append(str1*str2)
        elif(i == '/'):
            stack.append(str1/str2)

result = stack[0]
print(f'{result:.2f}')            

        
    
    
