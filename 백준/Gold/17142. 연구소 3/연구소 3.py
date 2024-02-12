from itertools import combinations
from collections import deque
import sys

def spread(lab, virus, N,count):
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    spread_time = 0
    queue = deque()
    zero = 0
    for _ in virus:
        queue.append((*_, 0))

    while queue:
        if zero == count:
            return spread_time
        x, y, time = queue.popleft()
        if lab[x][y] != 3 :
            lab[x][y] = 3
        for k in range(4):
            dx = x + di[k]
            dy = y + dj[k]
            if 0 <= dx < N and 0 <= dy < N and (lab[dx][dy] == 0 or lab[dx][dy] == 2):
                if lab[dx][dy] == 0:
                    zero +=1
                lab[dx][dy] = 3
                spread_time = max(spread_time, time + 1)
                queue.append((dx, dy, time + 1))
                
        
    if any(0 in row for row in lab):
        return float('inf') 
    else:
        return spread_time

N, M = map(int, sys.stdin.readline().split())
laboratory = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

count = 0
virus = []
for i in range(N):
    for j in range(N):
        if laboratory[i][j] == 2:
            virus.append((i, j))
        if laboratory[i][j] == 0:
            count+=1
lists = list(combinations(virus, M))
time = float('inf')


for _ in lists:
    lab = [row[:] for row in laboratory]
    min_time = spread(lab, _, N,count)
    time = min(time, min_time)

if time == float('inf'):
    print(-1)
else:
    print(time)
