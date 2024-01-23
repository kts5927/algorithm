import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
beaver = []
hedgehog = []
watersource = []
rock = []
for i in range(R):
    a = sys.stdin.readline().strip()
    for j in range(len(a)):
        if a[j] == 'D':
            beaver.append([i, j])
        elif a[j] == 'S':
            hedgehog.append([i, j, 0])
        elif a[j] == '*':
            watersource.append([i, j, 0])
        elif a[j] == 'X':
            rock.append([i,j])
            
que = deque(watersource)
table = [[0]*C for _ in range(R)]
while que:
    i,j,time = que.popleft()
    time += 1
    for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
        ni,nj = i + di , j + dj
        if 0 <= ni < R and 0 <= nj < C  and table[ni][nj] == 0 and [ni, nj] not in rock and [ni,nj] not in beaver:
            table[ni][nj] = time
            que.append((ni,nj,time))


ans = True
escape = deque(hedgehog)
past = [[0]* C for _ in range(R)]

while ans:

    if len(escape) == 0 :
        ans = False
        print('KAKTUS')
        continue
    x,y,turn = escape.popleft()
    turn +=1
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx,ny = x + dx , y + dy
        if nx == beaver[0][0] and ny == beaver[0][1] :
            print(turn)
            ans = False
        elif 0 <= nx < R and 0 <= ny < C and (table[nx][ny] > turn or table[nx][ny] == 0) and [nx,ny] not in rock and  past[nx][ny] != 1 :
            escape.append ((nx,ny,turn))
            past[nx][ny] = 1
