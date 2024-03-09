import sys
import copy
from collections import deque
N , M = map(int,sys.stdin.readline().split())
setting = [list(map(str,sys.stdin.readline().strip())) for _ in range(N)]
seq = deque()
visit = []

red = []
blue = []
for i in range(N):
    for j in range(M):
        if setting[i][j] == 'R':
            red = [i,j]
        if setting[i][j] == 'B':
            blue = [i,j]
seq.append([setting , red , blue , 0 , True , True])
ans = []
dx = [1 , -1 , 0 , 0]
dy = [0 , 0 , 1 , -1]
    
while seq:
    bord , red , blue , count  , red_l , blue_l= seq.popleft()
    
    if bord not in visit:
        visit.append(bord)
        for i in range(4):
            red_move = copy.deepcopy(red)
            red_live = copy.deepcopy(red_l)
            blue_move = copy.deepcopy(blue)
            blue_live = copy.deepcopy(blue_l)
            shadow = copy.deepcopy(bord)
        
            while True:
                
                if shadow[blue_move[0] + dx[i]][blue_move[1] + dy[i]] == '.' and shadow[blue_move[0]][blue_move[1]] == 'B':
                    shadow[blue_move[0] + dx[i]][blue_move[1] + dy[i]] = 'B'
                    shadow[blue_move[0]][blue_move[1]] = '.'
                    blue_move[0] += dx[i]
                    blue_move[1] += dy[i]
                
                if shadow[blue_move[0] + dx[i]][blue_move[1] + dy[i]] == 'O':
                    shadow[blue_move[0]][blue_move[1]] = '.'
                    blue_live = False
                    break
                
                if shadow[red_move[0]][red_move[1]] == 'R' and shadow[red_move[0] + dx[i]][red_move[1] + dy[i]] == '.':
                    shadow[red_move[0]][red_move[1]] = '.'
                    shadow[red_move[0] + dx[i]][red_move[1] + dy[i]] = 'R'

                    red_move[0] += dx[i]
                    red_move[1] += dy[i]

                    
                
                if shadow[red_move[0]][red_move[1]] == 'R' and shadow[red_move[0] + dx[i]][red_move[1] + dy[i]] == 'O':
                    shadow[red_move[0]][red_move[1]] = '.'
                    red_live = False
                
                if shadow[blue_move[0] + dx[i]][blue_move[1] + dy[i]] != '.' and not red_live:
                    break
                   
                if shadow[red_move[0] + dx[i]][red_move[1] + dy[i]] != '.' and shadow[blue_move[0] + dx[i]][blue_move[1] + dy[i]] != '.' and  red_live and blue_live:
                    break

            if  shadow not in visit and red_live and blue_live and count < 9:
                seq.append([shadow , red_move , blue_move , count+1 , red_live , blue_live])
            elif not red_live and blue_live:
                ans.append(count+1) 
                break
    if ans:
        break

if len(ans) == 0: 
    print(-1)
else:                 
    print(*ans)

