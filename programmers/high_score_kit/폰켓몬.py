def solution(nums):
    n = len(nums)/2
    distinct = set(nums)
    
    if n > len(distinct):
        return len(distinct)
    else:
        return n