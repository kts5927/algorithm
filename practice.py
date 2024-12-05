def solve(N, sequence):
    if N % 2 == 1:
        return "YES"
    
    even, odd = 0, 0
    for i, value in enumerate(sequence):
        if value == 1:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    
    return "YES" if -1 <= (even - odd) <= 1 else "NO"

T = int(input())  
results = []

for _ in range(T):
    data = list(map(int, input().split()))
    N = data[0] 
    sequence = data[1:]  
    results.append(solve(N, sequence))

print("\n".join(results))

