def cal(a, b, c):
    return a**2 + b**2 + c**2 + 7 * min(a, b, c)

def find_max(a, b, c, d):
    ans = 0
    ans = max(ans, cal(a + d, b, c))
    ans = max(ans, cal(a, b + d, c))
    ans = max(ans, cal(a, b, c + d))
    
    if d <= 10:
        for i in range(d + 1):
            for j in range(d - i + 1):
                k = d - i - j
                ans = max(ans, cal(a + i, b + j, c + k))
                ans = max(ans, cal(a + i, b + k, c + j))
                ans = max(ans, cal(a + j, b + i, c + k))
                ans = max(ans, cal(a + j, b + k, c + i))
                ans = max(ans, cal(a + k, b + i, c + j))
                ans = max(ans, cal(a + k, b + j, c + i))
    
    return ans

n = int(input())
players = [list(map(int, input().split())) for _ in range(n)]

for a, b, c, d in players:
    print(find_max(a, b, c, d))
