import sys
import heapq

def sharkwave (x , y , speed , direction):
    x_res = x
    y_res = y
    
    if direction == 3 or direction == 4:
        x_move = dx[direction]*speed
        if direction == 3:
            if (x + x_move) > C:
            
                if ((x + x_move-1)//(C-1))%2 == 1:
                    x_res = (x + x_move-1)%(C-1)
                    direction = 4
                else:
                    x_res = C-(x + x_move-1)%(C-1)
                    
            else:
                x_res = x + x_move
            
        elif direction == 4:
            if (x + x_move) <= 0:
                
                if ((-C - x - x_move)//(C-1))%2 == 1:
                    x_res = -(-C - x - x_move)//(C-1)
                    if(C - x - x_move)%(C-1)==0:
                        x_res += (C-1)
                    x_res += 1
                else:
                    x_res = C-(C - x + x_move)%(C-1)
                    if(C - x - x_move)%(C-1)==0:
                        x_res -= (C-1)
                    direction = 3
                        
            else:
                x_res = x + x_move


    else:
        y_move = dy[direction]*speed
        if direction == 2:
            if (y + y_move) > R:
            
                if ((y + y_move-1)//(R-1))%2 == 1:
                    y_res = (y + y_move-1)%(R-1)
                    direction = 1
                else:
                    y_res = R-(y + y_move-1)%(R-1)
                    
            else:
                y_res = y + y_move
            
        elif direction == 1:
            if (y + y_move) <= 0:
                
                if ((R - y + y_move)//(R-1))%2 == 1:
                    y_res = -(R - y - y_move)%(R-1)
                    if(R - y - y_move)%(R-1)==0:
                        y_res += (R-1)
                    direction = 2
                else:
                    y_res = R-(R - y + y_move)%(R-1)
                    if(R - y - y_move)%(R-1)==0:
                        y_res -= (R-1)
                    
                        
            else:
                y_res = y + y_move
    return x_res , y_res, direction
    



R , C , M = map(int,sys.stdin.readline().split())

shark_even = []
shark_odd = []
for _ in range(M):
    heapq.heappush(shark_even , list(map(int,sys.stdin.readline().split())))

human = 0
dx = [0 , 0 , 0 , 1 , -1]
dy = [0 , -1 , 1 , 0 , 0]

count = 0
    

while human <= C:
    print()
    for i in shark_even:
        print(*i, end='\n')
    # fishing shark_even
    fishing = True
    sharks = [[[]for _ in range(C+1)] for _ in range(R+1)]
    for i in sharks:
        print(*i, end='\n')
    human += 1
    # for i in sharks:
        # print(*i , end = '\n')
    while shark_even:
        y , x , speed , direction , size = heapq.heappop(shark_even)
        if fishing and x == human:
            fishing = False
            count += size
            print('catch : ',x,y)
            continue
        print(y,x,direction,speed)
        x,y,direction = sharkwave(x,y,speed,direction)
        print(y,x,direction,speed)
        print()
        if len(sharks[y][x]) == 0 or sharks[y][x][2] <= size:
            sharks[y][x] = [speed,direction,size]
    for i in sharks:
        print(*i,end='\n')

    for q in range(R):
        for w in range(C):
            if len(sharks[q][w]) > 0:
                heapq.heappush(shark_odd, [w,q,sharks[q][w][0],sharks[q][w][1],sharks[q][w][2]])
    
    print()
    for i in shark_odd:
        print(*i, end='\n')
    print(count)
       
    if human <= C:
        break
    
    fishing = True
    sharks = [[[]for _ in range(C+1)] for _ in range(R+1)]
    human += 1
    while shark_odd:
        x , y , speed , direction , size = heapq.heappop(shark_odd)
        if fishing and y == human:
            fishing = False
            count += size
            print('catch : ',x,y)
            continue
        print(x,y)
        if len(sharks[x][y]) == 0 or sharks[x][y][2] <= size:
            sharks[x][y] = [speed,direction,size]
            for i in sharks:
                print(*i,end='\n')
        
        
    for q in range(R):
        for w in range(C):
            if len(sharks[q][w]) > 0:
                heapq.heappush(shark_even, [q,w,sharks[q][w][0],sharks[q][w][1],sharks[q][w][2]])
       
       
print(count)
    
    
    
    
# import sys

# sys.setrecursionlimit(10 ** 8)
# input = lambda: sys.stdin.readline().rstrip()


# def fish(j):
#     for i in range(R):
#         if board[i][j]:
#             x = board[i][j][2]
#             board[i][j] = 0
#             return x
#     return 0


# def move():
#     global board  # board[i][j] 안에는 (s,d,z)의 값이 들어있음. 상어가 없는 경우엔 0이 들어있음
#     new_board = [[0 for _ in range(C)] for _ in range(R)]  # 상어들의 새 위치를 담을 공간
#     for i in range(R):
#         for j in range(C):
#             if board[i][j]:
#                 # 이 상어의 다음 위치는
#                 ni, nj, nd = get_next_loc(i, j, board[i][j][0], board[i][j][1])
#                 if new_board[ni][nj]:
#                     new_board[ni][nj] = max(
#                         new_board[ni][nj],
#                         (board[i][j][0], nd, board[i][j][2]),
#                         key=lambda x: x[2],
#                     )
#                 else:
#                     new_board[ni][nj] = (board[i][j][0], nd, board[i][j][2])

#     board = new_board  # board가 이제 상어들의 새 위치를 가리키도록

# def get_next_loc(i, j, speed, dir):

#     if dir == UP or dir == DOWN:  # i
#         cycle = R * 2 - 2
#         if dir == UP:
#             speed += 2 * (R - 1) - i
#         else:
#             speed += i

#         speed %= cycle
#         if speed >= R:
#             return (2 * R - 2 - speed, j, UP)
#         return (speed, j, DOWN)

#     else:  # j
#         cycle = C * 2 - 2
#         if dir == LEFT:
#             speed += 2 * (C - 1) - j
#         else:
#             speed += j

#         speed %= cycle
#         if speed >= C:
#             return (i, 2 * C - 2 - speed, LEFT)
#         return (i, speed, RIGHT)


# UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4
# R, C, M = map(int, input().split())
# board = [[0 for _ in range(C)] for _ in range(R)]

# for i in range(M):
#     r, c, s, d, z = map(int, input().split())
#     r, c = r - 1, c - 1
#     board[r][c] = (s, d, z)
#     # s : speed
#     # d : 1(up), 2(down), 3(right), 4(left)
#     # z : size


# ans = 0
# for j in range(C):
#     ans += fish(j)
#     move()

# print(ans)