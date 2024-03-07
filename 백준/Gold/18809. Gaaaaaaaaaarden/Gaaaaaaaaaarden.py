import copy
from itertools import combinations
from collections import deque
N , M , G , R = map(int,input().split())
garden = [list(map(int,input().split())) for _ in range(N)]
plant = []
lst = set()

def spread(G , R):
    cal = 0
    for i in range(N):
        for j in range(M):
            if garden[i][j] == 2:
                plant.append((i , j))
    plant_copy = set(plant)
    for green in combinations(plant , G):
        ground_nogreen = list(plant_copy - set(green))
        green_list = list(green)
        for red in combinations(ground_nogreen , R):
            red_list = list(red)
            result = blossom(green_list , red_list)
            if cal < result:
                cal = result
    return cal

def blossom(green_list , red_list):
    shadow = [[0 for _ in range(M)] for _ in range(N)]
    for i in green_list:
        shadow[i[0]][i[1]] = 1
    for i in red_list:
        shadow[i[0]][i[1]] = 2
 
    count = 0
    dx = [1 , -1 , 0 , 0]
    dy = [0 , 0 , 1 , -1]
    location = deque()
    
    
    for i in range(N):
        for j in range(M):
            if shadow[i][j] == 1 or shadow[i][j] == 2:
                location.append([i , j , 1])
    timer = 0
    spread = [[0 for _ in range(M)]for _ in range(N)]
    while location:
        i , j , time = location.popleft()   
        for k in range(4):
            x = dx[k] + i
            y = dy[k] + j
            if 0 <= x < N and 0 <= y < M and garden[x][y] != 0:
                if shadow[x][y] == 0   and shadow[i][j] != 3:
                    shadow[x][y] += shadow[i][j]
                    spread[x][y] = time
                    location.append([x,y,time+1])
                    
                elif shadow[x][y] == 1 and shadow[i][j] == 2 and spread[x][y] == time:
                    shadow[x][y] = 3
                    count +=1
                elif shadow[x][y] == 2 and shadow[i][j] == 1 and spread[x][y] == time:
                    shadow[x][y] = 3
                    count +=1
            
    return count
                
print(spread( G , R))