INF = int(1e9)

N, M, T, D = map(int, input().split())
mountain = [list(map(lambda x: ord(x) - ord('A') if 'A' <= x <= 'Z' else ord(x) - ord('a') + 26, input().strip())) for _ in range(N)]

di = [(-1, 0), (1, 0), (0, -1), (0, 1)]

graph = [[INF] * (N * M) for _ in range(N * M)]

def location(x, y):
    return x * M + y

for i in range(N):
    for j in range(M):
        now = location(i, j)
        for dx, dy in di:
            nx, ny = i + dx, j + dy
            if 0 <= nx < N and 0 <= ny < M:
                next = location(nx, ny)
                height = mountain[nx][ny] - mountain[i][j]
                if abs(height) <= T:
                    if height > 0:
                        cost = height ** 2
                    else:
                        cost = 1
                    graph[now][next] = cost

for i in range(N * M):
    graph[i][i] = 0

for k in range(N * M):
    for i in range(N * M):
        for j in range(N * M):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

max_height = mountain[0][0]

for i in range(N):
    for j in range(M):
        now = location(i, j)
        if graph[0][now] + graph[now][0] <= D:
            max_height = max(max_height, mountain[i][j])

print(max_height)
