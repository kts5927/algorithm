import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, -1, 0, 0, 1, 1]
dy = [0, 1, -1, 1, -1, 0]

def painting(x, y):
    global ans
    
    neighbor = [False for _ in range(9)]  
    for i in range(6):
        X = x + dx[i]
        Y = y + dy[i]
        
        if 0 <= X < N and 0 <= Y < N and hive[X][Y].isdigit(): 
            neighbor[int(hive[X][Y])] = True  
    
    for i in range(1, 9):
        if not neighbor[i]: 
            ans[i] = True
            hive[x][y] = str(i) 
            break

def solve(i, j):
    que = deque([(i, j)])  
    while que:
        x, y = que.popleft()
        painting(x,y)
        for i in range(6):
            X = x + dx[i]
            Y = y + dy[i]
            
            if 0 <= X < N and 0 <= Y < N and hive[X][Y] == "X": 
                painting(X, Y)
                que.append((X, Y))  

N = int(input())
hive = [list(input().strip()) for _ in range(N)]  
ans = [False for _ in range(9)]

for i in range(N):
    for j in range(N):
        if hive[i][j] == "X":
            solve(i, j)

Ans = 0
for i in ans:
    if i == True:
        Ans += 1
        
if Ans < 4:
    print(Ans)
else:
    print(3)
