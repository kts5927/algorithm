from collections import deque
import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
ddx = [1, 1, -1, -1]
ddy = [-1, 1, 1, -1]

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
X = int(sys.stdin.readline().strip())

que = deque([(0, 0)])
visited = [[False] * M for _ in range(N)]
visited[0][0] = True

alive = False

while que:
    x, y = que.popleft()

    if x == (N - 1) and y == (M - 1):
        alive = True
        break

    for i in range(1, X + 1):
        for j in range(4):
            nx = x + (dx[j] * i)
            ny = y + (dy[j] * i)

            for k in range(i):
                nnx = nx + (ddx[j] * k)
                nny = ny + (ddy[j] * k)
                if 0 <= nnx < N and 0 <= nny < M and not visited[nnx][nny] and lst[nnx][nny] == lst[x][y]:
                    que.append((nnx, nny))
                    visited[nnx][nny] = True

if alive:
    print("ALIVE")
else:
    print("DEAD")
