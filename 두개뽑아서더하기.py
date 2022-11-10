numli = [5,0,2,7]

def solution(numbers):
    
    temp = []
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            temp.append(numbers[i]+numbers[j])
    
    #중복제거
    for num in temp:
        if num not in answer:
            answer.append(num)
    
    print(answer)
    return sorted(answer)
        

        

print(solution(numli))