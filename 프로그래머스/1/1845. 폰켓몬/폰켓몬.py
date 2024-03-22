def solution(nums):
    
    answer = 0
    
    n = len(nums)/2
    nums.sort()
    count = 0
    number = 0
    for i in nums:
        if number != i:
            count += 1
            number = i
    
    if count >= n:
        answer = n
    else : 
        answer = count
    
    return answer