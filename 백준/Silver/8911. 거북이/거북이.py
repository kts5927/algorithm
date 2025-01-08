import sys
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

T = int(input())
for i in range(T):
    move = list(map(str,input().strip()))
    
    direction = 0
    X = 0
    Y = 0
    MaxX = 0
    MaxY = 0
    MinX = 0
    MinY = 0
    for i in move:
        if i == 'F':
            X += dx[direction]
            Y += dy[direction]
            
            MaxX = max(MaxX,X)
            MinX = min(MinX,X)
            MaxY = max(MaxY,Y)
            MinY = min(MinY,Y)
            
        elif i == 'B':
            X -= dx[direction]
            Y -= dy[direction]
            
            MaxX = max(MaxX,X)
            MinX = min(MinX,X)
            MaxY = max(MaxY,Y)
            MinY = min(MinY,Y)
        elif i == 'L':
            direction = (direction + 3) % 4
        elif i == 'R':
            direction = (direction + 1) % 4
            
    print((MaxX-MinX) * (MaxY-MinY))
    