N , M = map(int,input().split())
item = [list(map(int,input().split())) for _ in range(N)]
backpack = [int(input()) for _ in range(M)]

K = max(backpack)
cal = [[0 for _ in range(K + 1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        if 0 <= j - item[i-1][0] <= K:
            cal[i][j] = max(cal[i-1][j] , cal[i-1][j-item[i-1][0]] + item[i-1][1])
        else : cal[i][j] = cal[i-1][j]




ans = []
count = 1
for i in backpack:
    ans.append([cal[N][i]/i , count])
    count += 1
ans.sort(key = lambda x:(-x[0] , x[1]))
print(ans[0][1])

