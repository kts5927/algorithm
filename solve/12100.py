from itertools import product

def move(command, puzzle:list):
    line_ud = [0 for _ in range(N)]
    line_lr = [0 for _ in range(N)]
    if command == 'up':
        
        for i in range(N):
            for j in range(N):
                
                if line_ud[j] != puzzle[i][j]:
                    if puzzle[i][j] != 0:
                        line_ud[j] = puzzle[i][j]
                    for k in range(0,i):
                        if puzzle[k][j] == 0:
                            puzzle[k][j] = puzzle[i][j]
                            puzzle[i][j] = 0
                            break
                elif line_ud[j] == puzzle[i][j]:
                    line_ud[j] *= 2
                    for k in range(i-1,-1,-1):
                        if puzzle[k][j] == puzzle[i][j]:
                            puzzle[k][j] *= 2
                            puzzle[i][j] = 0
                            line_ud[j] = 0
                            break
                        
    elif command == 'down':
        
        for i in range(N-1,-1,-1):
            for j in range(N-1,-1,-1):
                
                if line_ud[j] != puzzle[i][j]:
                    if puzzle[i][j] != 0:
                        line_ud[j] = puzzle[i][j]
                    for k in range(N-1,i,-1):
                        if puzzle[k][j] == 0:
                            puzzle[k][j] = puzzle[i][j]
                            puzzle[i][j] = 0
                            if puzzle[k][j] != 0:
                                break
                elif line_ud[j] == puzzle[i][j]:
                    line_ud[j] *= 2
                    for k in range(i+1,N):
                        if puzzle[k][j] == puzzle[i][j]:
                            puzzle[k][j] *= 2
                            puzzle[i][j] = 0
                            line_ud[j] = 0
                            break
                        
    elif command == 'left':
        
        for i in range(N):
            for j in range(N):
                
                if line_lr[i] != puzzle[i][j]:
                    if puzzle[i][j] != 0:
                        line_lr[i] = puzzle[i][j]
                    for k in range(0,j):
                        if puzzle[i][k] == 0:
                            puzzle[i][k] = puzzle[i][j]
                            puzzle[i][j] = 0
                            break
                elif line_lr[i] == puzzle[i][j]:
                    line_lr[i] *= 2
                    for k in range(j-1,-1,-1):
                        if puzzle[i][k] == puzzle[i][j]:
                            puzzle[i][k] *= 2
                            puzzle[i][j] = 0
                            line_lr[i] = 0
                            break
                        
    elif command == 'right':
        
        for i in range(N-1,-1,-1):
            for j in range(N-1,-1,-1):
                
                if line_lr[i] != puzzle[i][j]:
                    if puzzle[i][j] != 0:
                        line_lr[i] = puzzle[i][j]
                    for k in range(N-1,j,-1):
                        if puzzle[i][k] == 0:
                            puzzle[i][k] = puzzle[i][j]
                            puzzle[i][j] = 0
                            if puzzle[i][k] != 0: 
                                break
                elif line_lr[i] == puzzle[i][j]:
                    line_lr[i] *= 2
                    for k in range(j+1,N):
                        if puzzle[i][k] == puzzle[i][j]:
                            puzzle[i][k] *= 2
                            puzzle[i][j] = 0
                            line_lr[i] = 0
                            break
                        

                    
    
    # print()
    # for i in puzzle:
    #     print(*i,end='\n')
    # print()
    return puzzle 
            
            
            
            
            
            
N = int(input()) 
puzzle = [list(map(int,input().split())) for _ in range(N)]

commands = ['up','down','right','left']
input_command = list(product(commands,repeat = 5))
ans = 0
for q in input_command:
    shadow = [i[:] for i in puzzle]
    for w in list(q):
        shadow  = move(w,shadow)
        
    max_num = 0
    for i in range(N):
        for j in range(N):
            if max_num < shadow[i][j]:
                max_num = shadow[i][j]   
                    

    if ans < max_num:
        ans = max_num
            
print(ans)


# 9
# 2 2 2 1 2 2 2
# 2 2 2 1 2 2 2
# 2 2 2 1 2 2 2
# 1 1 1 1 1 1 1
# 2 2 2 1 2 2 2
# 2 2 2 1 2 2 2
# 2 2 2 1 2 2 2
 