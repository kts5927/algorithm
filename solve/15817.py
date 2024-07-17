import sys

N , x = map(int,sys.stdin.readline().split())
dp = [0 for _ in range(x+1)]
dp[0] = 1
for i in range(N):
    a , b = map(int,sys.stdin.readline().split())
    for i in range(x,0,-1):
        p = 0
        for j in range(a,x,a):
            if i-j >= 0:
                dp[i] += dp[i-j]


print(dp[x])


