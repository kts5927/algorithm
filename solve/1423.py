import sys
from collections import deque
N = int(sys.stdin.readline())

arr = [[[0] for _ in range(N)] for _ in range(N)]
edge = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
past = [False for _ in range(N+1)]
seq = deque()

for i in range(N):
    arr[i] = list(map(int,sys.stdin.readline().strip()))
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            edge[j+1].append(i+1)
            visited[i+1] +=1

rutebreaker = True
while past.count(False) != 1:
    for i in range(N,0,-1):
        if visited[i] == 0 and  not past[i]:
            seq.append(i)
            past[i] = True
            for j in range(len(edge[i])):
                visited[edge[i][j]] -= 1
            break
    if past.count(True) == visited.count(0)-1 and past.count(True) != N:
        rutebreaker = False
        break

ans = [0 for _ in range(N+1)]
if rutebreaker:
    for i in range(1,N+1):
        a = seq.pop()
        ans[a] = i 

    print(*ans[1:])
else : print(-1)
