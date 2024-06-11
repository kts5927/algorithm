from collections import deque

N, M = map(int, input().split())

target = [list(map(int, input().strip())) for _ in range(N)]
deq = deque()
for i in range(N):
    for j in range(M):
        if target[i][j] == 1:
            deq.append([i, j])
ans = (-1, -1)
max_distance = 10

while deq:
    x, y = deq.popleft()
    hit = [0 for _ in range(max_distance)]
    dup = False
    for i in range(N):
        for j in range(M):
            location = max(abs(y - j), abs(x - i))
            if target[i][j] == 1:
                if location < max_distance:
                    if hit[location] == 0:
                        hit[location] = 1
                    elif hit[location] == 1:
                        dup = True
                        break
        if dup:
            break
    if sum(hit) == max_distance and not dup:
        ans = (x, y)
        break

if ans != (-1, -1):
    print(ans[0], ans[1])
else:
    print(-1)
