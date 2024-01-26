import sys
N,M = map(int,sys.stdin.readline().split())
stone = []

for i in range(M):
    a = int(sys.stdin.readline())
    stone.append(a)
table = [[10001]* (int((2*N)**0.5)+2)  for _ in range(N+1)]

table[1][0] = 0
for i in range(2,N+1):
    if i in stone : 
        continue
    for j in range(int((2*N)**0.5)+1):
        table[i][j] = min(table[i-j][j-1],table[i-j][j],table[i-j][j+1])+1
        
ans = min(table[N])
if ans == 10001:
    print(-1)
else:
    print(ans)