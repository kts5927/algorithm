import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
shadow = [[0] * M for _ in range(N)]
cd = deque([(0, 0)])  # (0, 0)에서 시작
shadow[0][0] = 1

while cd:
    i, j = cd.popleft()
    

    if j > 0 and shadow[i][j-1] == 0 and maze[i][j-1] != 0:
        cd.append((i, j-1))
        shadow[i][j-1] = shadow[i][j] + 1
    if j < M-1 and shadow[i][j+1] == 0 and maze[i][j+1] != 0:
        cd.append((i, j+1))
        shadow[i][j+1] = shadow[i][j] + 1
    if i > 0 and shadow[i-1][j] == 0 and maze[i-1][j] != 0:
        cd.append((i-1, j))
        shadow[i-1][j] = shadow[i][j] + 1
    if i < N-1 and shadow[i+1][j] == 0 and maze[i+1][j] != 0:
        cd.append((i+1, j))
        shadow[i+1][j] = shadow[i][j] + 1
    if i == N-1 and j == M-1:
        break

print(shadow[N-1][M-1])