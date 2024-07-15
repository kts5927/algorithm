from collections import deque

N = int(input())
lst = list(map(str,input().strip()))

world = deque()
world.append(['.'])
x = 0
y = 0
wide = 1
height = 1
direction = 0

dx = [0,-1,0,1]
dy = [1,0,-1,0]

for i in lst:
    
    if i == 'R':
        direction += 1
        direction %= 4
        
    elif i == 'L':
        direction += 3
        direction %= 4
        
    else:
        
        if y+dy[direction] < 0:
            y += 1
            world.appendleft(['#']*wide)
            height += 1
        elif y+dy[direction] >= height:
            world.append(['#']*wide)
            height += 1
        elif x+dx[direction] < 0:
            x += 1
            for i in world:
                i.insert(0, '#')
            wide += 1
        elif x+dx[direction] >= wide:
            for i in world:
                i.append('#')
            wide += 1
        world[y+dy[direction]][x+dx[direction]] = '.'
        y += dy[direction]
        x += dx[direction]
        
        
for i in world:
    print(''.join(i))