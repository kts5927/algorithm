def max_score(n, notes):
    dp = [-float('inf')] * (n + 1)
    
    k_1 = 0
    k_2 = 0
    
    dp[1] = notes[0]
    
    for i in range(1, n):
        t = notes[i]
        tmp = -float('inf')
        
        for j in range(i, 0, -1):
            tmp = max(tmp, dp[j])
            if j + 1 <= n:
                dp[j + 1] = dp[j] + (j + 1) * t
        
        dp[0] = max(k_1, k_2)
        dp[1] = dp[0] + t
        
        k_2 = k_1
        k_1 = tmp
    
    tmp = max(k_1, k_2)
    
    for i in range(1, n + 1):
        tmp = max(tmp, dp[i])
    
    return max(tmp, 0)

n = int(input())
notes = list(map(int, input().split()))

print(max_score(n, notes))