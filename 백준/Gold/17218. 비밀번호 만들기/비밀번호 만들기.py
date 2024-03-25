str1 = list(str(input().strip()))
str2 = list(str(input().strip()))

len1 = len(str1)
len2 = len(str2)

dp = [[0 for _ in range(len1+1)] for _ in range(len2+1)]

for i in range(1,len2+1):
    for j in range(1,len1+1):
        
        if str1[j-1] == str2[i-1]:  
            dp[i][j] = max(dp[i-1][j-1] + 1 , dp[i][j-1])
        else : dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
    
j , i = len1 , len2

ans = []
while i>0 and j>0:
    if dp[i-1][j] == dp[i][j-1] == dp[i-1][j-1] == dp[i][j]:
        i -= 1
        j -= 1    
    elif dp[i-1][j] > dp[i][j-1]:
        i-=1
    elif dp[i-1][j] < dp[i][j-1]:
        j-=1
    else:
        ans.append(str1[j-1])
        i-=1
        j-=1
ans.reverse()
ans = ''.join(ans)

print(ans)