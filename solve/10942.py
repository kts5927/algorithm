import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
dp = [[0]*N for _ in range(N)]

for i in range(N):
    dp[i][i]=1

for i in range(N-1):
    if lst[i]==lst[i+1]: 
        dp[i][i+1]=1
    else: 
        dp[i][i+1]=0

for i in range(N-2):
    for j in range(N-2-i):
        k = j+2+i
        if lst[j]==lst[k] and dp[j+1][k-1]==1:

            dp[j][k]=1

T = int(sys.stdin.readline())
for i in range(T):
    
    a, b = map(int, sys.stdin.readline().split())
    print(dp[a-1][b-1])