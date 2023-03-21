def solution(arr):
    answer = []
    for num in arr:
        if not answer:
            answer.append(num)
        if num != answer[-1]:
            answer.append(num)
    
    return answer
        
# test
arr = [1,1,3,3,0,1,1]
print(solution(arr))