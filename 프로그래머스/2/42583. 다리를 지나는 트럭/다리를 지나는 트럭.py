from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = [0 for _ in range(bridge_length)]
    bridge = deque(bridge)
    truck_weights = deque(truck_weights)
    sum_ = 0
    while True:
        
        a = bridge.popleft()
        bridge.append(0)
        sum_ -= a
        
        if len(truck_weights) > 0 and weight - sum_ >= truck_weights[0]:
            bridge[-1] = truck_weights[0]
            sum_ += truck_weights[0]
            truck_weights.popleft()
        answer += 1
        
        if len(truck_weights) == 0 and sum_ == 0:
            break
    
    return answer