def f(a, b, c):
    return a**2 + b**2 + c**2 + 7 * min(a, b, c)

def calculate_score(a, b, c, d):
    ans = 0
    ans = max(ans, f(a + d, b, c))
    ans = max(ans, f(a, b + d, c))
    ans = max(ans, f(a, b, c + d))
    
    if d <= 1000:
        for i in range(d + 1):
            for j in range(d - i + 1):
                k = d - i - j
                ans = max(ans, f(a + i, b + j, c + k))
                ans = max(ans, f(a + i, b + k, c + j))
                ans = max(ans, f(a + j, b + i, c + k))
                ans = max(ans, f(a + j, b + k, c + i))
                ans = max(ans, f(a + k, b + i, c + j))
                ans = max(ans, f(a + k, b + j, c + i))
    
    return ans

# 입력 받기
n = int(input())
players = [tuple(map(int, input().split())) for _ in range(n)]

# 각 플레이어의 최대 점수 계산
for a, b, c, d in players:
    print(calculate_score(a, b, c, d))
