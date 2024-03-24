from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = [0 for _ in range(bridge_length)]
    bridge = deque(bridge)
    truck_weights = deque(truck_weights)

    while True:
        print(bridge)
        print(truck_weights)
        a = bridge.popleft()
        bridge.append(0)
        
        if len(truck_weights) > 0 and weight - sum(bridge) > truck_weights[0]:
            bridge[-1] = truck_weights[0]
            truck_weights.popleft()
        answer += 1
        
        if len(truck_weights) == 0 and sum(bridge) == 0:
            break
    
    return answer

print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))