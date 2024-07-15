import sys

N , M = map(int,sys.stdin.readline().split())
lst = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

LR = [0]*M
UD = [0]*N
ans = 1
for i in range(N):
    
    a = (lst[i][0]-1)//M
    count = 0
    for j in range(M):
        if a*M < lst[i][j] <= (a+1)*M:
            count += 1 
    if count != M:
        ans = 0
        break

if ans:
    for j in range(M):
        a = lst[0][j] % M
        count = 0
        for i in range(N):
            if lst[i][j]%M == a:
                count += 1
        if count != N:
            ans = 0
            break
print(ans)