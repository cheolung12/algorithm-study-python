import math

def solution(progresses, speeds):
    remain = []
    for i, j in zip(progresses, speeds):
        remain.append(math.ceil((100-i)/j))
    
    temp = 0
    answer = []
    for i in remain:
        if temp == 0 or i>temp:
            temp = i
            answer.append(1)
            continue
        else:
            answer[-1] += 1
    
    return answer




# test
prograsses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(prograsses, speeds))

