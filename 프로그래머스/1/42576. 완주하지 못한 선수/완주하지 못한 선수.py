def solution(participant, completion):
    answer = 0
    participant.sort()
    completion.sort()
    for i in range(len(participant)-1):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    if answer == 0:
        answer = participant[-1]
    
    return answer