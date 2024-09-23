import sys
from collections import deque


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def DFS(a,b):
    count = 1
    que = deque()
    que.append([a,b])
    
    while que:
        x,y = que.popleft()
        for i in range(4):
            X = x+dx[i]
            Y = y+dy[i]
            if 0 <= X < N and 0 <= Y < N and farm[Y][X] == 0:
                que.append([X,Y])
                farm[Y][X] = 2
                count += 1
    
    ret = count // K
    if count%K != 0:
        ret += 1
    return ret
    



N , M , K = map(int,sys.stdin.readline().split())
farm = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        if farm[i][j] == 0:
            farm[i][j] = 2
            ans += DFS(j,i)


cal = M - ans
if cal >= 0 and ans > 0:
    print('POSSIBLE')
    print(cal)
    
else:
    print('IMPOSSIBLE')