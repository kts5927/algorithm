import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

lists = [[0 for _ in range(N+1)] for _ in range(N+1)]
destination = [0 for _ in range(N+1)]
destination[0] = 1
container = [False for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    destination[b] += 1
    lists[a][b] = c
    container[a] = True

seq = deque()
visited = [False for _ in range(N+1)]
while destination.count(0) < N:
    for i in range(1, N+1):
        if destination[i] == 0 and not visited[i]and container[i]:
            seq.append(i)
            visited[i] = True
            for j in range(1, N+1):
                if lists[i][j] != 0 :
                    destination[j] -= 1
seq.popleft()

for i in lists:
    print(i)
while True:
    a = seq.popleft()
    for i in range(1,N+1):
        lists[N][i] += lists[a][i]*lists[N][a]
        
    lists[N][a] = 0   
        
    if len(seq)  == 0:
        break   


for i in range(1,N+1):
    if not container[i]:
        print(i ,lists[N][i])
    