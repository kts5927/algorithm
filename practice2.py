import sys
input = sys.stdin.readline

def function(p):
    m, j = len(p), 0
    pi = [0]*m
    for i in range(1, m):
        while j > 0 and p[i]!=p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            j+=1
            pi[i] = j
    return pi


long = input().rstrip()
N = int(input())
string = []
string_cal = []
for i in range(N):
    string.append(input().rstrip())
    string_cal.append(function(string[i]))
dp = [0 for _ in range(len(long))]
fail = [0 for _ in range(501)]

for i in range(len(long)):
    dp[i] = dp[i-1]
    for j in range(N):
        m = len(string[j])
        while fail[j] > 0 and string[j][fail[j]] != long[i]:
            fail[j] = string_cal[j][fail[j]-1]
        if long[i] == string[j][fail[j]]:
            if fail[j] == m - 1:
                t = dp[i-m] if i-m>=0 else 0
                dp[i] = max(dp[i], t+m)
                fail[j] = string_cal[j][fail[j]]
            else:
                fail[j]+=1
print(dp[-1])