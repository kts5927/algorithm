n = int(input())
rating = [int(input()) for _ in range(n)]

dp = [0] * n

for i in range(n):
    dp[i] = rating[i] 
    for j in range(i):
        if rating[j] < rating[i]:  
            dp[i] = max(dp[i], dp[j] + rating[i])

print(max(dp))
