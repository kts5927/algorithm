def solution(answers):
    problem = len(answers)
    
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5] 
    c = [3,3,1,1,2,2,4,4,5,5] 
    
    first = []
    second = []
    third = []
    
    for i in range(problem):
        first.append(a[i%5])
        second.append(b[i%8])
        third.append(c[i%10])
    
    
    score1 = 0
    score2 = 0
    score3 = 0
    
    for i in range(problem):
        if answers[i] == first[i]:
            score1 += 1
        if answers[i] == second[i]:
            score2 += 1
        if answers[i] == third[i]:
            score3 += 1
            
    ans = [score1 , score2 , score3]
    max_ = max(ans)
    
    answer = []
    if score1 == max_:
        answer.append(1)
    if score2 == max_:
        answer.append(2)
    if score3 == max_:
        answer.append(3)
        
        
    return answer