import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    Rectangle = [list(map(int, input().split())) for _ in range(N)]

    cal = [[0] * M for _ in range(N)]

    for i in range(N - 1, -1, -1):
        for j in range(M - 1, -1, -1):
            down = cal[i + 1][j] if i + 1 < N else 0
            right = cal[i][j + 1] if j + 1 < M else 0
            diag = cal[i + 1][j + 1] if i + 1 < N and j + 1 < M else 0

            cal[i][j] = Rectangle[i][j] + down + right - diag

    result = max(max(row) for row in cal)
    print(result)
