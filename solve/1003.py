dp = [0 for _ in range(100)]
dp[0] = 1
dp[1] = 1
for i in range(2,41):
    dp[i] = dp[i-1] + dp[i-2]


T = int(input())
for i in range(T):
    N = int(input())
    if N == 0:
        print(0 , 1)
    elif N == 1:
        print(1 , 0)
    else:
        print(dp[N-1],dp[N-2])