def LCS_3(LCS1, LCS2, LCS3):
    len1, len2, len3 = len(LCS1), len(LCS2), len(LCS3)
    
    DP = [[[0 for _ in range(len3 + 1)] for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            for k in range(1, len3 + 1):
                if LCS1[i - 1] == LCS2[j - 1] == LCS3[k - 1]:
                    DP[i][j][k] = DP[i - 1][j - 1][k - 1] + 1
                else:
                    DP[i][j][k] = max(DP[i - 1][j][k], DP[i][j - 1][k], DP[i][j][k - 1])

    return DP[len1][len2][len3]

LCS1 = input().strip()
LCS2 = input().strip()
LCS3 = input().strip()

print(LCS_3(LCS1, LCS2, LCS3))
