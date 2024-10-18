def max_brightness(N, a, b):
    initial_brightness = sum(a[i] for i in range(N) if b[i] == 1)
    
    change = [0] * N
    for i in range(N):
        if b[i] == 1:
            change[i] = -a[i]
        else:
            change[i] = a[i]
    
    max_change = -float('inf')
    current_sum = 0
    
    for i in range(N):
        current_sum += change[i]
        max_change = max(max_change, current_sum)
        if current_sum < 0:
            current_sum = 0
    
    return initial_brightness + max_change

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(max_brightness(N, a, b))
