# 백준  https://www.acmicpc.net/problem/

import sys
from collections import deque
N , M = map(int,sys.stdin.readline().split())
procession = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]

def BFS(procession , i , j , k , shadow):
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[i][j] = True

    count = 0
    lists = deque()
    lists.append([i,j])    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while lists:
        a , b = lists.popleft()
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0 <= x < N and 0 <= y < M  and procession[x][y] == 0 and not visited[x][y]:
                lists.append([x,y])
                visited[x][y] = True
                count += 1
                
    visited = [[False for _ in range(M)] for _ in range(N)]
    lists.append([i,j])                
    while lists:
        a , b = lists.popleft()
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0 <= x < N and 0 <= y < M  and procession[x][y] == 0 and not visited[x][y]:
                lists.append([x,y])
                visited[x][y] = True
                procession[x][y] = count
                shadow[x][y] = k


def cal(procession , i , j):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for k in range(4):
        x = dx[k] + i
        y = dy[k] + j
        if  0 <= x < N and 0 <= y < M and procession[x][y] != "W":
            procession[i][j] += procession[x][y]
            

shadow = [[0 for _ in range(M)] for _ in range(N)]
k = 0
for i in range(N):
    for j in range(M):
        if procession[i][j] == 0:
            BFS(procession , i , j , k , shadow)
        if procession[i][j] == 1:
            procession[i][j] = "W"
            
for i in range(N):
    for j in range(M):
        if procession[i][j] == "W":
            cal(procession , i , j)


for _ in shadow:
    print(*_ , sep ='')
    
    
import sys
from collections import deque
N , M = map(int,sys.stdin.readline().split())
table = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]



def BFS(table , move , shadow ,  i , j ,number ):
    que = deque()
    que.append([i , j])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = [[False for _ in range(M)] for _ in range(N)]
    
    count = 1
    while que:
        a , b = que.popleft()
        visited[a][b] = True
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0<= x < N and 0 <= y < M and table[x][y] == 0 and not visited[x][y]:
                que.append([x,y])
                count += 1 
                
    visited = [[False for _ in range(M)] for _ in range(N)]
    que.append([i,j])
    while que:
        a , b = que.popleft()
        visited[a][b] = True 
        move[a][b] = count
        shadow[a][b] = number
            
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0<= x < N and 0 <= y < M and table[x][y] == 0 and not visited[x][y]:
                que.append([x,y])
                
number = 0
shadow = [[0 for _ in range(M)] for _ in range(N)]
move = [[0 for _ in range(M)] for _ in range(N)]
arr = []

for i in range(N):
    for j in range(M):
        if table[i][j] == 0 and shadow[i][j] == 0:
            BFS(table , shadow , move , i , j , number)
            number += 1
                      
ans = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        arr = set()
        if table[i][j] == 1:
            ans[i][j] += 1
        for k in range(4):
            x = dx[k] + i
            y = dy[k] + j
            if 0<= x < N and 0 <= y < M and table[i][j] == 1: 
                if move[x][y] not in arr:
                    ans[i][j] += shadow[x][y]
                    arr.add(move[x][y])

for _ in ans:
    print(*_ , sep = '')


