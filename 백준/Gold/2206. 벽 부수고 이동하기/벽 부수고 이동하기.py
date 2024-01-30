from collections import deque

N, M = map(int, input().split())
table = []
for _ in range(N):
    row = list(map(int, input().strip()))
    table.append(row)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]

queue = deque([(0, 0, 1)])  
visited[0][0][1] = True

while queue:
    x, y, bricks = queue.popleft()

    if N == 1 and M == 1:
            print(1)
            exit()
    if x == N - 1 and y == M - 1:
        
        print(visited[x][y][bricks])
        exit()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny][bricks]:
            if table[nx][ny] == 0:
                visited[nx][ny][bricks] = visited[x][y][bricks] + 1
                queue.append((nx, ny, bricks))
            elif bricks:
                visited[nx][ny][0] = visited[x][y][bricks] + 1
                queue.append((nx, ny, 0))

print(-1)
