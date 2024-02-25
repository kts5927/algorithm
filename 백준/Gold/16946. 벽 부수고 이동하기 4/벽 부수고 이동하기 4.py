import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
shadow = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False] * M for _ in range(N)]
place = {}
place[0] = 0

def BFS(i, j):
    que = deque()
    que.append([i,j])
    count = 1
    while que:
        a, b = que.popleft()
        shadow[a][b] = group
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0 <= x < N and 0 <= y < M and not visited[x][y] and table[x][y] == 0:
                que.append((x, y))
                visited[x][y] = True
                count += 1
    return count

group = 1
for i in range(N):
    for j in range(M):
        if table[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            cnt = BFS(i, j)
            place[group] = cnt
            group += 1

for i in range(N):
    for j in range(M):
        if table[i][j] == 1:
            neighbors = set()
            for k in range(4):
                x = dx[k] + i
                y = dy[k] + j
                if 0 <= x < N and 0 <= y < M:
                    neighbors.add(shadow[x][y])
            for z in neighbors:
                table[i][j] += place[z]
            table[i][j] %= 10

for row in table:
    print(*row, sep='')
