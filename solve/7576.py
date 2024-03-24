from collections import deque

M , N = map(int,input().split())

tomato = [list(map(int,input().split())) for _ in range(N)]
location = deque()
count = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            location.append([i , j , 0])
        if tomato[i][j] == 0:
            count += 1

dx = [1 , -1 , 0 , 0]
dy = [0 , 0 , 1 , -1]

ans = 0
time = 0



while location:
    i , j , time  = location.popleft()
    print(location)
    for k in range(4):
        x = dx[k] + j
        y = dy[k] + i
        
        if 0 <= x < M and 0 <= y < N and tomato[y][x] == 0:
            tomato[y][x] = 1
            location.append([y , x , time+1])
            count -= 1
            ans = time+1
    
if count != 0:
    print(-1)
else : print(time)

