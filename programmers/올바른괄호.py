def solution(s):
    stack = []
    if s[0] == ')':
        return False
    
    for b in s:
        if b == '(':
            stack.append(s)
        else:
            if not stack:
                return False
            stack.pop()
            
    if not stack:
        return True
    else:
        return False
    

# test
s = "()()"
print(solution(s))