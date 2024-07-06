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
    
# test1 = 'winlose???winl???w??'
# test2 = 'win'
# test1 = '???cab?????'
# test2 = 'abcab'
# test1 = 'glo?yto?e??an?'
# test2 = 'or'


lst1 = list(map(str,sys.stdin.readline().rstrip()))
lst2 = list(map(str,sys.stdin.readline().rstrip()))
l1_len = len(lst1)
l2_len = len(lst2)
dp = [[0 for _ in range(l1_len)] for _ in range(l2_len+1)]

# print(lst1)
# print(lst2)

for i in range(l2_len):
    for j in range(l1_len):
        if lst1[j] == lst2[i]:
            dp[i][j] = i+1
            dp[-1][j] = 1
        if lst1[j] == '?':
            dp[i][j] = i+1

cal = fail(lst2)


# for i in dp:
#     print(i)
    
    
ans = 0
i = 0

while i < l1_len:
    x = i
    y = 0
    if dp[y][x] != 0:
        while y < l2_len and x < l1_len:
            if dp[y][x] == l2_len:
                i = x+1
                y = cal[y]
                ans+=1
                break
                
            if dp[y][x] != 0:
                x+=1
                y+=1
            else:
                i+=1
                x = cal[y]
                break
    else:
        i+=1
    
    if x >= l1_len:
        break
            
print(ans)