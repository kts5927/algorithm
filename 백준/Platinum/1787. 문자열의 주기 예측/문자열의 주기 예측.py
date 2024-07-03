import sys

def kmp(S):
    fail = [0] * len(S)
    j = 0
    for i in range(1, len(S)):
        while (j > 0 and S[i] != S[j]):
            j = fail[j - 1]
        if S[i] == S[j]:
            j += 1
            fail[i] = j
    return fail

def cal(S, fail):
    lst = [0] * len(S)
    for i in range(1, len(S)):
        k = i + 1
        if fail[fail[k - 1] - 1] > 0:
            lst[i] = lst[fail[k - 1] - 1]
        else:
            lst[i] = fail[k - 1]
    return lst

N = int(sys.stdin.readline())
S = sys.stdin.readline().strip()

fail = kmp(S)
lst = cal(S, fail)

ans = 0
for i in range(1, N):
    if not lst[i]:
        continue
    if i + 1 - lst[i] >= lst[i]:
        ans += i + 1 - lst[i]
print(ans)
