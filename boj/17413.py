import sys
input = sys.stdin.readline

result = ""     
stack = ""      
tag = False

for i in input().rstrip():
    if (i == '<'):
        tag = True
        result += stack[::-1]
        stack = ""
        result += i
        continue
    elif(i == '>'):
        tag = False
        result += i
        continue
    elif(i == ' '):
        result += stack[::-1]
        result += " "
        stack = ""
        continue

    if tag:
        result += i
    else:
        stack += i


print(result + stack[::-1])
