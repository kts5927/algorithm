import sys
from collections import deque
N = int(sys.stdin.readline())

RGB = [list(map(str,sys.stdin.readline().strip())) for _ in range(N)]
RB = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if RGB[i][j] != 'G':
            RB[i][j] = RGB[i][j] 
        else :
            RB[i][j] = 'R'

lst = deque()
count_RGB = 0
count_RB = 0
dx = [1 , -1 , 0 , 0]
dy = [0 , 0 , 1 , -1]

for i in range(N):
    for j in range(N):
        if RGB[i][j] != 0:
            count_RGB += 1
            lst.append([i , j , RGB[i][j]])
            RGB[i][j] = 0
            while lst:

                di , dj , color = lst.popleft()
                
                for k in range(4):
                    x = di + dx[k]
                    y = dj + dy[k]
                    
                    if 0 <= x < N and 0 <= y < N and RGB[x][y] == color:
                        lst.append([x , y , color])
                        RGB[x][y] = 0
                        
for i in range(N):
    for j in range(N):
        if RB[i][j] != 0:
            count_RB += 1
            lst.append([i , j , RB[i][j]])
            RB[i][j] = 0
            while lst:

                di , dj , color = lst.popleft()
                
                for k in range(4):
                    x = di + dx[k]
                    y = dj + dy[k]
                    
                    if 0 <= x < N and 0 <= y < N and RB[x][y] == color:
                        lst.append([x , y , color])
                        RB[x][y] = 0
                        
                        
                        
                        
print(count_RGB , count_RB)