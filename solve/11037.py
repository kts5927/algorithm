import sys

def DFS(num, cal, used_digits):
    global ans
    
    if cal > 987654321 or cal > num * 1.5:
        return 
    
    if num < cal:
        ans = min(ans, cal)
        return
    
    for i in range(1, 10):
        if not used_digits[i]: 
            used_digits[i] = True
            DFS(num, cal * 10 + i, used_digits)
            used_digits[i] = False 

for line in sys.stdin:
    N = int(line.strip())
    ans = float('inf')
    DFS(N, 0, [False] * 10)  
    if ans == float('inf'):
        ans = 0
    print(ans)
