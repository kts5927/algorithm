def solution(progresses, speeds):
    answer = []
    i = 0
    time = 0
    while i < len(progresses):
        
        cal = []
        while i < len(progresses):
            if progresses[i] + time*speeds[i] >= 100:
                cal.append(progresses[i])
                i += 1
            else : break
        if len(cal) != 0:
            answer.append(len(cal))
        time += 1
    
    return answer