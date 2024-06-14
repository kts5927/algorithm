import sys
from collections import deque
N , M = map(int,sys.stdin.readline().split())

lst = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
count = 0
largest = 0

for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            deq = deque()
            deq.append([i,j])
            lst[i][j] = 0
            range_ = 1
            while deq:
                a,b = deq.popleft()
                for k in range(4):
                    x = dx[k] + b
                    y = dy[k] + a
                    if 0 <= x < M and 0 <= y < N and lst[y][x] == 1:
                        lst[y][x] = 0
                        deq.append([y,x])
                        range_ += 1
            count += 1
            largest = max(range_ , largest)
print(count)
print(largest)