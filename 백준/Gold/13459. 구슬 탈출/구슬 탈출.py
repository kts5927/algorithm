from collections import deque

def move (first, second):
    if lst[first[0]+dx[i]][first[1]+dy[i]] == '.' and second != [first[0]+dx[i],first[1]+dy[i]]:
        return [first[0]+dx[i],first[1]+dy[i]]
    else:
        return first

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
visited = [[RED_location,BLUE_location]]
ans = 0

while que:
    RED , BLUE , count = que.popleft()
    if count >= 10:
        continue
    for i in range(4):            
        BLUE_CAL = [BLUE[0],BLUE[1]]
        RED_CAL = [RED[0],RED[1]]
        
        while True:
            
            if lst[BLUE_CAL[0]+dx[i]][BLUE_CAL[1]+dy[i]] == 'O':
                BLUE_CAL = False 
                RED_CAL = False
                ans = 0
                break
            
            BLUE_CAL = move(BLUE_CAL,RED_CAL)
            
            if  ans == 0:
                if lst[RED_CAL[0]+dx[i]][RED_CAL[1]+dy[i]] == 'O':
                    RED_CAL = [RED_CAL[0]+dx[i],RED_CAL[1]+dy[i]]
                    ans = 1

                RED_CAL = move(RED_CAL,BLUE_CAL)
            if ans == 0 and (lst[BLUE_CAL[0]+dx[i]][BLUE_CAL[1]+dy[i]] == '#' or [BLUE_CAL[0]+dx[i],BLUE_CAL[1]+dy[i]] == RED_CAL ) and (lst[RED_CAL[0]+dx[i]][RED_CAL[1]+dy[i]] == '#' or [RED_CAL[0]+dx[i],RED_CAL[1]+dy[i]] == BLUE_CAL):
                break
            
            if ans != 0 and lst[BLUE_CAL[0]+dx[i]][BLUE_CAL[1]+dy[i]] == '#':
                break
       
        if ans != 0 :
            break
        if [RED_CAL,BLUE_CAL] not in visited and RED_CAL:
            visited.append([RED_CAL,BLUE_CAL])
            que.append([RED_CAL,BLUE_CAL,count+1])
    if ans != 0:
        break
print(ans)