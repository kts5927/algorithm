from collections import deque

N , M = map(int,input().split())

lst = [list(map(str,input().strip())) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(N):
    for j in range(M):
        if lst[i][j] == 'R':
            RED_location = [i,j]
            lst[i][j] = '.'
        elif lst[i][j] == 'B':
            BLUE_location = [i,j]
            lst[i][j] = '.'

que = deque()
que.append([RED_location,BLUE_location,0])

while que:
    RED , BLUE , count = que.popleft()
    for i in range(4):
        if i == 1:
            if BLUE[0] >= RED[0]:
                
                BLUE_CAL = [BLUE[0],BLUE[1]]
                RED_CAL = [RED[0],RED[1]]
                
                while True:
                    
                    if BLUE_CAL[1] + 1 < M and RED_CAL[1] + 1 < M :
                        
                        if lst[BLUE_CAL[0]][BLUE_CAL[1]+1] != '.':
                            BLUE_CAL = [BLUE_CAL[0],BLUE_CAL[1]+1]
                            
                        if lst[RED_CAL[0]][RED_CAL[1]+1] != '.':
                            RRED_CALED = [RED_CAL[0],RED_CAL[1]+1]
            else : 
                
                BLUE_CAL = [BLUE[0],BLUE[1]]
                RED_CAL = [RED[0],RED[1]]
                
                while True:
                    
                    if BLUE_CAL[1] + 1 < M and RED_CAL[1] + 1 < M :
                        
                        if lst[RED_CAL[0]][RED_CAL[1]+1] != '.':
                            RRED_CALED = [RED_CAL[0],RED_CAL[1]+1]
                        
                        if lst[BLUE_CAL[0]][BLUE_CAL[1]+1] == '.':
                            BLUE_CAL = [BLUE_CAL[0],BLUE_CAL[1]+1]
        if i == 2:
            if BLUE[0] >= RED[0]:
                
                BLUE_CAL = [BLUE[0],BLUE[1]]
                RED_CAL = [RED[0],RED[1]]
                
                while True:
                    
                    if BLUE_CAL[1] + 1 < M and RED_CAL[1] + 1 < M :
                        
                        if lst[BLUE_CAL[0]][BLUE_CAL[1]+1] != '.':
                            BLUE_CAL = [BLUE_CAL[0],BLUE_CAL[1]+1]
                            
                        if lst[RED_CAL[0]][RED_CAL[1]+1] != '.':
                            RRED_CALED = [RED_CAL[0],RED_CAL[1]+1]
            else : 
                
                BLUE_CAL = [BLUE[0],BLUE[1]]
                RED_CAL = [RED[0],RED[1]]
                
                while True:
                    
                    if BLUE_CAL[1] + 1 < M and RED_CAL[1] + 1 < M :
                        
                        if lst[RED_CAL[0]][RED_CAL[1]+1] != '.':
                            RRED_CALED = [RED_CAL[0],RED_CAL[1]+1]
                        
                        if lst[BLUE_CAL[0]][BLUE_CAL[1]+1] == '.':
                            BLUE_CAL = [BLUE_CAL[0],BLUE_CAL[1]+1]
        if i == 3:
            if BLUE[0] >= RED[0]:
                
                BLUE_CAL = [BLUE[0],BLUE[1]]
                RED_CAL = [RED[0],RED[1]]
                
                while True:
                    
                    if BLUE_CAL[1] + 1 < M and RED_CAL[1] + 1 < M :
                        
                        if lst[BLUE_CAL[0]][BLUE_CAL[1]+1] != '.':
                            BLUE_CAL = [BLUE_CAL[0],BLUE_CAL[1]+1]
                            
                        if lst[RED_CAL[0]][RED_CAL[1]+1] != '.':
                            RRED_CALED = [RED_CAL[0],RED_CAL[1]+1]
            else : 
                
                BLUE_CAL = [BLUE[0],BLUE[1]]
                RED_CAL = [RED[0],RED[1]]
                
                while True:
                    
                    if BLUE_CAL[1] + 1 < M and RED_CAL[1] + 1 < M :
                        
                        if lst[RED_CAL[0]][RED_CAL[1]+1] != '.':
                            RRED_CALED = [RED_CAL[0],RED_CAL[1]+1]
                        
                        if lst[BLUE_CAL[0]][BLUE_CAL[1]+1] == '.':
                            BLUE_CAL = [BLUE_CAL[0],BLUE_CAL[1]+1]
        if i == 4:
            if BLUE[0] >= RED[0]:
                
                BLUE_CAL = [BLUE[0],BLUE[1]]
                RED_CAL = [RED[0],RED[1]]
                
                while True:
                    
                    if BLUE_CAL[1] + 1 < M and RED_CAL[1] + 1 < M :
                        
                        if lst[BLUE_CAL[0]][BLUE_CAL[1]+1] != '.':
                            BLUE_CAL = [BLUE_CAL[0],BLUE_CAL[1]+1]
                            
                        if lst[RED_CAL[0]][RED_CAL[1]+1] != '.':
                            RRED_CALED = [RED_CAL[0],RED_CAL[1]+1]
            else : 
                
                BLUE_CAL = [BLUE[0],BLUE[1]]
                RED_CAL = [RED[0],RED[1]]
                
                while True:
                    
                    if BLUE_CAL[1] + 1 < M and RED_CAL[1] + 1 < M :
                        
                        if lst[RED_CAL[0]][RED_CAL[1]+1] != '.':
                            RRED_CALED = [RED_CAL[0],RED_CAL[1]+1]
                        
                        if lst[BLUE_CAL[0]][BLUE_CAL[1]+1] == '.':
                            BLUE_CAL = [BLUE_CAL[0],BLUE_CAL[1]+1]
                            
