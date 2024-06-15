import sys
from collections import deque
N , M = map(int,sys.stdin.readline().split())
lst = [list(map(str,sys.stdin.readline().strip())) for _ in range(N)]

dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,1,1,1,0,-1,-1,-1]

deq = deque()
for i in range(N):
    for j in range(M):
        if lst[i][j] == 'E' or lst[i][j] == 'I':
            deq.append([i,j])
    
ans = 0
while deq:
    a,b = deq.popleft()
    for i in range(8):
        if 0 <= dx[i] + b < M and 0 <= dy[i] + a < N and (lst[dy[i] + a][dx[i] + b] == 'N' or lst[dy[i] + a][dx[i] + b] == 'S'):
            if 0 <= 2*dx[i] + b < M and 0 <= 2*dy[i] + a < N and (lst[2*dy[i] + a][2*dx[i] + b] == 'F' or lst[2*dy[i] + a][2*dx[i] + b] == 'T'):
                if 0 <= 3*dx[i] + b < M and 0 <= 3*dy[i] + a < N and (lst[3*dy[i] + a][3*dx[i] + b] == 'P' or lst[3*dy[i] + a][3*dx[i] + b] == 'J'):
                    ans += 1
                    
print(ans)