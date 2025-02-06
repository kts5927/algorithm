A = input()
B = input()
a = len(A)
b = len(B)

dp = [[0] * (b+1) for _ in range(a+1)]

for i in range(a+1):
    dp[i][0] = i
for i in range(b+1):
    dp[0][i] = i
    
for i in range(1,a+1):
    for j in range(1,b+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1],min(dp[i-1][j],dp[i][j-1]))+1

            
print(dp[a][b])