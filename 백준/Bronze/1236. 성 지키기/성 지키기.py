N , M = map(int,input().split())
lst = [list(map(str,input().strip())) for _ in range(N)]

UD = ['.'] * N
LR = ['.'] * M

for i in range(N):
    
    for j in range(M):
        if lst[i][j] == 'X':
            UD[i] = 'X'
            LR[j] = 'X'
            
first = 0
for i in UD:
    if i == '.':
        first += 1
second = 0
for i in LR:
    if i == '.':
        second += 1

print(max(first,second))