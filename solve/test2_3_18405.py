import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
table = []

for _ in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    table.append(a)

S, X, Y = map(int, sys.stdin.readline().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
for number in range(1,K+1):
    for i in range(N):
        for j in range(N):
            if table[i][j] == number:
                queue.append((table[i][j], 0, i, j))

while queue:
    virus, time, x, y = queue.popleft()
    if time == S:
        break

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and table[nx][ny] == 0:
            table[nx][ny] = virus
            queue.append((virus, time + 1, nx, ny))
print(table[X-1][Y-1])
