import sys
from collections import deque
input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def check(a,b,count):
    que = deque()
    que.append([a,b])
    lst[a][b] = count
    num = 1
    while que:
        x,y = que.popleft()
        
        for i in range(4):
            X = x+dx[i]
            Y = y+dy[i]
            
            if 0 <= X < N and 0 <= Y < M and lst[X][Y] == 1:
                lst[X][Y] = count
                que.append([X,Y])
                num += 1
    return num
                
def ans_cal(a,b):
    
    count = 0
    buffer = []
    for i in range(4):
        x = a+dx[i]
        y = b+dy[i]
        
        if 0 <= x < N and 0 <= y < M and lst[x][y] != 0 and lst[x][y] not in buffer:
            count += count_list[lst[x][y]-2]
            buffer.append(lst[x][y])
    return count
            
N , M = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]

count_list = []
count = 2
for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            count_list.append(check(i,j,count))
            count += 1
            
ans = 0
for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:
            ans = max(ans_cal(i,j),ans)
            
print(ans+1)