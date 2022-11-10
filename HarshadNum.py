def solution(x):
    num_list = []
    for i in str(x):
        num_list.append(int(i))
    
    sum_list = sum(num_list)

    if(x % sum_list == 0):
        return True
    else:
        return False
