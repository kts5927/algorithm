import sys

N, M = map(int, sys.stdin.readline().split())
tile = []
shadow = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    a = list(map(str, sys.stdin.readline().strip()))
    tile.append(a)

count = 0

def calculate(tile, count, shadow, i, j, N, direction):
    if direction == '-':
        if j > 0 and tile[i][j-1] == '-' and shadow[i][j-1] == 0:
            shadow[i][j-1] = 1
            calculate(tile, count, shadow, i, j-1, N, direction)
        elif j < M-1 and tile[i][j+1] == '-' and shadow[i][j+1] == 0:
            shadow[i][j+1] = 1
            calculate(tile, count, shadow, i, j+1, N, direction)
    elif direction == '|':
        if i > 0 and tile[i-1][j] == '|' and shadow[i-1][j] == 0:
            shadow[i-1][j] = 1
            calculate(tile, count, shadow, i-1, j, N, direction)
        elif i < N-1 and tile[i+1][j] == '|' and shadow[i+1][j] == 0:
            shadow[i+1][j] = 1
            calculate(tile, count, shadow, i+1, j, N, direction)

for i in range(N):
    for j in range(M):
        if tile[i][j] == '-' and shadow[i][j] == 0:
            count += 1
            shadow[i][j] = 1
            calculate(tile, count, shadow, i, j, N, '-')
        elif tile[i][j] == '|' and shadow[i][j] == 0:
            count += 1
            shadow[i][j] = 1
            calculate(tile, count, shadow, i, j, N, '|')

print(count)