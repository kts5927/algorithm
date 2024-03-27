from collections import deque
from itertools import combinations
N , M = map(int,input().split())
science_facility = [list(map(int , input().split())) for _ in range(N)]
irradiate = []
empty = []

dx = [1 , -1 , 0 , 0]
dy = [0 , 0 , 1 , -1]


for i in range(N):
    for j in range(M):
        if science_facility[i][j] == 2:
            irradiate.append([i , j])
        elif science_facility[i][j] == 0:
            empty.append([i , j])
empty = list(combinations(empty , 3))
ans = 0
for k in empty:
    
    first , second , third = k
    replace = [i[:] for i in science_facility]
    replace[first[0]][first[1]] = 1
    replace[second[0]][second[1]] = 1
    replace[third[0]][third[1]] = 1
    virus = irradiate[:]
    virus = deque(virus)
    
    while virus:
        i , j = virus.popleft()
        
        for q in range(4):
            x = i + dx[q]
            y = j + dy[q]
            
            if 0 <= x < N and 0 <= y < M and replace[x][y] == 0:
                replace[x][y] = 2
                virus.append([x , y])
    count = 0            
    for i in range(N):
        for j in range(M):
            if replace[i][j] == 0:
                count += 1
    if ans < count:
        ans = count
        
print(ans)