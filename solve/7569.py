from collections import deque

M, N, H = map(int, input().split())
tomato = [[[0] * M for _ in range(N)] for _ in range(H)]

for i in range(H):
    for j in range(N):
        tomato[i][j] = list(map(int, input().split()))

queue = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                queue.append((i, j, k, 0)) 

while queue:
    i, j, k, time = queue.popleft()

    for di, dj, dk in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
        ni, nj, nk = i + di, j + dj, k + dk
        if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M and tomato[ni][nj][nk] == 0:
            tomato[ni][nj][nk] = 1
            queue.append((ni, nj, nk, time + 1))

if any(0 in row for layer in tomato for row in layer):
    print(-1)
else:
    print(time)