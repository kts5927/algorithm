import sys

def fail(p):
    m, j = len(p), 0
    l = [0]*m
    for i in range(1, m):
        while j > 0 and p[i]!=p[j]:
            j = l[j-1]
        if p[i] == p[j]:
            j+=1
            l[i] = j
    return l

lst1 = list(map(str,sys.stdin.readline().strip()))
lst2 = list(map(str,sys.stdin.readline().strip()))
l1_len = len(lst1)
l2_len = len(lst2)

LCS = [[i + 1 if lst1[j] == lst2[i] or lst1[j] == '?' else 0 for j in range(l1_len)] for i in range(l2_len)]
cal = fail(lst2)
i = 0
y = 0
point = [0]*l1_len
while i < l1_len :
    x = i
    if LCS[y][x] != 0:
        while y < l2_len and x < l1_len:
            if LCS[y][x] == l2_len:
                point[x] += 1
                i += 1
                y = 0
                break
            if LCS[y][x] != 0:
                x+=1
                y+=1
            else:
                i += 1
                y = 0
                break
    else:
        i+=1
        y = 0
    if x >= l1_len:
        break
a = 0
dp = [0]*l1_len
n = []
for i in range(l2_len):
    if cal[i] not in n:
        n.append(cal[i])
nn = len(n)


for i in range(l2_len-1,l1_len):
    dp[i] = point[i]
    dp[i] += a
    a = max(dp[i-l2_len] , a)
    if point[i] == 1:
        j = cal[l2_len - 1]
        while j > 0:
            dp[i] = max(dp[i], dp[i - l2_len + j] + 1)
            j = cal[j - 1]
        dp[i] = max(dp[i], a + 1)    
print(max(dp))