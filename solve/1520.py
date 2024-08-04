import sys
sys.setrecursionlimit(100000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    if x == M-1 and y == N-1: 
        return 1
    if dp[x][y] != -1: 
        return dp[x][y]
    
    ways = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and lst[nx][ny] < lst[x][y]:
            ways += dfs(nx, ny)
    
    dp[x][y] = ways
    return dp[x][y]

M, N = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1 for _ in range(N)] for _ in range(M)]

result = dfs(0, 0)
print(result)
