from collections import deque

def solution(priorities, location):
    que = deque((v,i) for i,v in enumerate(priorities))
    order = 0

    while(que):
        m = max(que)[0]
        item = que.popleft()
        if item[0] == m:
            order += 1
            if item[1] == location:
                return order
            else:
                continue
        else:
            que.append(item)

# test
p = [1, 1, 9, 1, 1, 1]
l = 0
solution(p,l)