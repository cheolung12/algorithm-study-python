survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]

def solution(survey, choices):
    
    types = dict(
        R = 0, T = 0,
        C = 0, F = 0,
        J = 0, M = 0,
        A = 0, N = 0
    )

    # 점수 계산
    for i in range(len(survey)):
        if(choices[i] == 1):
            types[survey[i][0]] += 1
        elif(choices[i] == 2):
            types[survey[i][0]] += 2
        elif(choices[i] == 3):
            types[survey[i][0]] += 3
        elif(choices[i] == 4):
            continue
        elif(choices[i] == 5):
            types[survey[i][1]] += 1
        elif(choices[i] == 6):
            types[survey[i][1]] += 2
        elif(choices[i] == 7):
            types[survey[i][1]] += 3
        
    answer = ""
    answer += "R" if types['R'] >= types['T'] else "T"
    answer += "C" if types['C'] >= types['F'] else "F"
    answer += "J" if types['J'] >= types['M'] else "M"
    answer += "A" if types['A'] >= types['N'] else "N"

    return answer

print(solution(survey, choices))
   
