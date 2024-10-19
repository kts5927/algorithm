import sys

def DFS(num, cal, used_digits):
    if cal > 987654321:
        return float('inf')
    
    min_val = float('inf')
    if cal > num:
        min_val = cal
    
    for i in range(1, 10):
        if i not in used_digits:
            used_digits.add(i)
            cal_next = DFS(num, cal * 10 + i, used_digits)
            min_val = min(min_val, cal_next)
            used_digits.remove(i)  # 백트래킹
            
    return min_val

for line in sys.stdin:
    N = int(line.strip())
    result = DFS(N, 0, set())
    if result == float('inf'):
        print(0)
    else:
        print(result)
