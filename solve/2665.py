import sys
from collections import deque
n = int(sys.stdin.readline())
table = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
shadow = [[float("inf")]*n for _ in range(n)]
shadow[0][0] = 0
route = deque([[0, 0]])
while route:
    
    x,y = route.popleft()
    if x < n-1  and shadow[x+1][y] > shadow[x][y] :
        if table[x+1][y] == 0 :
            shadow[x+1][y] = min(shadow[x][y] + 1,shadow[x+1][y])
        elif table[x+1][y] == 1:
            shadow[x+1][y] = shadow[x][y]
        route.append([x+1,y])    
    if y < n-1 and shadow[x][y+1] > shadow[x][y]:
        if table[x][y+1] == 0 :
            shadow[x][y+1] = min(shadow[x][y] + 1,shadow[x][y+1])
        elif table[x][y+1] == 1:
            shadow[x][y+1] = shadow[x][y]
        route.append([x,y+1])
    if x > 0  and shadow[x-1][y] > shadow[x][y] :
        if table[x-1][y] == 0 :
            shadow[x-1][y] = min(shadow[x][y] + 1,shadow[x-1][y])
        elif table[x-1][y] == 1:
            shadow[x-1][y] = shadow[x][y]
        route.append([x-1,y])
    if y >0 and shadow[x][y-1] > shadow[x][y]:
        if table[x][y-1] == 0 :
            shadow[x][y-1] = min(shadow[x][y] + 1,shadow[x][y-1])
        elif table[x][y-1] == 1:
            shadow[x][y-1] = shadow[x][y]
        route.append([x,y-1])
        

print(shadow[n-1][n-1])