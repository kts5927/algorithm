import sys
import heapq

def sharkwave (x , y , speed , direction):
    x_res = x
    y_res = y
    
    if direction == 3 or direction == 4:
        x_move = dx[direction]*speed
        if direction == 3:
            if (x + x_move) > C:
            
                if ((x + x_move-1)//(C-1))%2 == 0:
                    x_res = (x + x_move-1)%(C-1)
                    x_res += 1
                else:
                    x_res = C-(x + x_move-1)%(C-1)
            else:
                x_res = x + x_move
            
        if direction == 4:
            if (x + x_move) < 0:
                
                if ((x + x_move)%C)//2 == 0:
                    x_res = -(x + x_move+1)%(C-1)
                else:
                    x_res = C + (x + x_move%C)%(C-1)
                    
            else:
                x_res = x + x_move
            
    
    else:
        y_move = dy[direction]*speed
        if direction == 1:
            if (y + y_move) > 0:
            
                if ((y + y_move)%C)//2 == 0:
                    y_res = (y + y_move + (y + y_move)//C)%C
                else:
                    y_res = (y + y_move + (y + y_move)//C)%C
                    
            else:
                y_res = y + y_move
        
        if direction == 2:
            if (y + y_move) < 0:
                
                if ((y + y_move)%C) // 2 == 0:
                    y_res = C - (y + y_move + (y + y_move)//C)%C
                else:
                    y_res = (y + y_move + (y + y_move)//C)%C
                    
            else:
                y_res = y + y_move
    
    
    return x_res , y_res
    



R , C , M = map(int,sys.stdin.readline().split())

shark_even = []
shark_odd = []
for _ in range(M):
    heapq.heappush(shark_even , list(map(int,sys.stdin.readline().split())))

human = 0
dx = [0 , 0 , 0 , 1 , -1]
dy = [0 , 1 , -1 , 0 , 0]

print()
while human >= 0:
    
    table = [[0 for _ in range(C)] for _ in range(R)]
    while shark_even:
        x , y , speed , direction , size = heapq.heappop(shark_even)
        x , y = sharkwave(x , y , speed, direction)
        
        print(x , y , direction)
    if human == 0:
        break
    human -= 1
    
