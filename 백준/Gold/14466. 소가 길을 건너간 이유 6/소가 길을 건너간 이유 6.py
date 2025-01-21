import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def meet(start,end):
    
    que = deque()
    que.append(start)
    visited = [[0 for i in range(N+1)] for j in range(N+1)]
    visited[start[0]][start[1]] = 1
    
    while que:
        x,y = que.popleft()
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0 < X < N+1 and 0 < Y < N+1 and visited[X][Y] == 0 and [X,Y] not in farm[x][y]:
                if X == end[0] and Y == end[1]:
                    return True
                que.append([X,Y])
                visited[X][Y] = 1
    
    return False



N,K,R = map(int,input().split())
farm = [[[] for i in range(N+1)] for j in range(N+1)]

for i in range(R):
    R,C,RR,CC = map(int,input().split())
    
    farm[R][C].append([RR,CC])
    farm[RR][CC].append([R,C])

    
cow = []
ans = 0
for i in range(K):
    cow.append(list(map(int,input().split())))
for i in range(len(cow)):
    for j in range(i+1,len(cow)):
        if meet(cow[i],cow[j]) == False:
            ans += 1


print(ans)