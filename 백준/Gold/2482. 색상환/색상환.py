N = int(input())
K = int(input())
def calculation(n) : 
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

    dp[1][0] = 1
    dp[1][1] = 1

    for i in range(N+1):
        for j in range(N+1):
            if j == 1 : dp[i][j] = i
            elif i>j : dp[i][j] = dp[i-1][j] + dp[i-2][j-1]
    return dp
ans = calculation(N)

if K == 1:
    print(N)
else:
    print((ans[N-3][K-1] + ans[N-1][K]) % 1000000003)        