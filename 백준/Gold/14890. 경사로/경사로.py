import sys
input = sys.stdin.readline

def check(lst: list, L: int) -> bool:
    n = len(lst)
    used = [False] * n  
    
    for i in range(1, n):
        diff = lst[i] - lst[i-1]
        
        if abs(diff) > 1:
            return False
        
        if diff == 1:
            for j in range(i-1, i-1-L, -1):
                if j < 0 or used[j] or lst[j] != lst[i-1]:
                    return False
                used[j] = True

        elif diff == -1:
            for j in range(i, i+L):
                if j >= n or used[j] or lst[j] != lst[i]:
                    return False
                used[j] = True
                
    return True

N, L = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]

count = 0

for row in road:
    if check(row, L):
        count += 1

for col in zip(*road):  
    if check(col, L):
        count += 1

print(count)
