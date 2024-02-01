N = int(input())
step = []
for _ in range(N):
    step.append(int(input()))
    
    
if N >= 3:    
    score = [0]* N
    score[0] = step[0]
    score[1] = step[1] + step[0]
    score[2] = max(step[0] + step[2] , step[1] + step[2])
    for i in range(3,N):
        score[i] = max(score[i-2] + step[i] , score[i-3] + step[i-1] + step[i])
    
    print(score[-1])
    
elif N == 2 :
    print(step[1] + step[0])
elif N == 1 :
    print(step[0])