import sys

def path():
    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + lst[i-1][j-1]

N = int(sys.stdin.readline().strip())
lst = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
dp = [[0] * (N+1) for _ in range(N+1)]

P = int(sys.stdin.readline().strip())
points = {tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(P)}

path()

for i in range(1, N+1):
    for j in range(1, N+1):
        if (i, j) not in points:
            dp[i][j] = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        if dp[i-1][j] != 0 or dp[i][j-1] != 0:
            dp[i][j] = max(dp[i][j],lst[i-1][j-1] + max(dp[i-1][j], dp[i][j-1]) )

print(dp[N][N])


for i in dp:
    print(i)