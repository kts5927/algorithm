import sys
from collections import deque

n = int(input())
maze = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
cal = [[n**2]*n for _ in range(n)]
cal[0][0] = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

deq = deque()
deq.append([0,0,0])

while deq:
    
    x,y,count = deq.popleft()
    
    for i in range(4):
        X = x+dx[i]
        Y = y+dy[i]
        if 0 <= X < n and 0 <= Y < n:
            new_count = count + (1 if maze[Y][X] == 0 else 0)
            if new_count < cal[Y][X]:
                cal[Y][X] = new_count
                deq.append([X, Y, new_count])

print(cal[-1][-1])