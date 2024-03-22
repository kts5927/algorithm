from collections import deque

def solution(priorities, location):
    answer = 0
    max_priority = max(priorities)  # 최대 우선 순위를 미리 계산

    jobs = deque((priority, i == location) for i, priority in enumerate(priorities))

    while jobs:
        priority, is_target = jobs.popleft()
        
        if priority < max_priority:
            jobs.append((priority, is_target))
        else:
            answer += 1
            if is_target:
                break
            max_priority = max(p for p, _ in jobs)  # 최대 우선 순위 갱신

    return answer