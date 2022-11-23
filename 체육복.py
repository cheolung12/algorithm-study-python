def solution(n, lost, reserve):
    
    li = [0] * n
    for i in lost:
        li[i-1] = -1
    for i in reserve:
        li[i-1] = li[i-1]+1
    
    for i in range(len(li)):
        if(li[i] == -1):
            if(i == 0 and li[i+1] == 1):    # 첫번째 사람이 체육복이 없는데 그 다음사람이 빌려줄 수 있는 경우
                li[i+1] = 0
                li[i] = 0
            elif(i == n-1 and li[i-1] == 1): # 마지막 사람이 체육복이 없는데 그 이전 사람이 빌려줄 수 있는 경우
                li[i-1] = 0
                li[i] = 0
            elif(i != 0 and i != n-1):      # 처음 마지막 x, 중간사람
                if(li[i-1] == 0 and li[i+1] == 0):
                    continue        # 왼쪽 오른쪽 둘 다 못 빌려주면 그냥 넘어간다
                elif(li[i-1] == 1 and li[i+1] == 1):  # 왼쪽 오른쪽 둘 다 빌려줄 수 있다면 왼쪽 사람거를 우선으로 받는다
                    li[i-1] = 0
                    li[i] = 0
                elif(li[i-1] == 1): # 왼쪽만 빌려줄 수 있는 경우
                    li[i-1] = 0
                    li[i] = 0
                elif(li[i+1] == 1): # 오른쪽만 빌려 줄 수 있는 경우
                    li[i+1] = 0
                    li[i] = 0
    answer = 0
    for stu in li:
        if(stu == 0 or stu == 1):
            answer += 1

    return answer

