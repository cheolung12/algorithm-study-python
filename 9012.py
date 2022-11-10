import sys
n = int(sys.stdin.readline())



for i in range(n):

    stack = []
    parentheses = sys.stdin.readline()

    for j in parentheses:
        if (j=='('):
            stack.append(j)
        elif(j==')'):
            if(len(stack)==0):
                print("NO")
                break
            else:
                stack.pop()
    else:   #break문으로 끊기지 않고 수행되었을 경우 실행
        if(len(stack)==0):
            print("YES") # 스택이 비어있음
        else:
            print("NO") # 스택에 괄호가 남아있음
        
        

        


