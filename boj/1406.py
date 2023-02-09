import sys

precon = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())
l_stack = []
r_stack = []

for i in precon:
    l_stack.append(i)

for i in range(n):
    command = sys.stdin.readline().split()
    
    if(command[0] == 'L'):
        if(not l_stack):
            pass
        else:
            r_stack.append(l_stack.pop())
    elif(command[0] == 'D'):
        if(not r_stack):
            pass
        else:
            l_stack.append(r_stack.pop())
    elif(command[0] == 'B'):
        if(not l_stack):
            pass
        else:
            l_stack.pop()
    elif(command[0] == 'P'):
        l_stack.append(command[1])

print("".join(l_stack + list(reversed(r_stack))))



    
# command가 'L' 이고 l_stack이 존재한다면~ (코드 수정 한 줄로)