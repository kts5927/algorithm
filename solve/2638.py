import sys
from collections import deque

def melt_cheese(N, M, cheese):
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    air = deque()
    air.append([0, 0])
    cloud = [[0 for _ in range(M)] for __ in range(N)]
    visit = [[False for _ in range(M)] for __ in range(N)]

    while air:
        x, y = air.popleft()

        for _ in range(4):
            dx = x + di[_]
            dy = y + dj[_]
            if 0 <= dx < N and 0 <= dy < M and not visit[dx][dy] and cheese[dx][dy] != 1:
                visit[dx][dy] = True
                air.append([dx, dy])
                cloud[dx][dy] = 2

    shadow = [[0 for _ in range(M)] for __ in range(N)]
    for i in range(N):
        for j in range(M):
            for _ in range(4):
                dx = i + di[_]
                dy = j + dj[_]
                if 0 <= dx < N and 0 <= dy < M and cloud[dx][dy] == 2:
                    shadow[i][j] += 1

    for i in range(N):
        for j in range(M):
            if shadow[i][j] >= 2:
                cheese[i][j] = 0

    return cheese

def main():
    N, M = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(N)]

    time = 1
    while True:
        melted_cheese = melt_cheese(N, M, cheese)
        if sum(sum(row) for row in melted_cheese) == 0:
            break
        cheese = melted_cheese
        time += 1

    print(time)

if __name__ == "__main__":
    main()
