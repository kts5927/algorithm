import sys
from collections import deque
from itertools import combinations
def find_destroy(lst):
    
    cost = float('inf')
    cal_lst = combinations(lst , M)
        
    for lists in cal_lst:
        cost = min(cost , find_cost(lists))
    return cost

def find_cost(lst):
    cal_chicken = [arr[:] for arr in chicken]
    for i in chicken_house:
        if i not in lst:
            cal_chicken[i[0]][i[1]] = 0
            

    cal = deque()    
    for i in lst:
        cal.append([i[0],i[1],0])
        
    ans = 0
    while cal:
        i , j , distance = cal.popleft()
        distance += 1
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < N and 0 <= y < N and cal_chicken[x][y] != 3:
                if cal_chicken[x][y] == 1:
                    ans += distance
                cal_chicken[x][y] = 3
                cal.append([x,y,distance])

    return ans
                    

N , M = map(int,sys.stdin.readline().split())
chicken = [list(map(int,sys.stdin.readline().split()))for _ in range(N)]
chicken_house = []
visited = []
count = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(N):
    for j in range(N):
        if chicken[i][j] == 2:
            chicken_house.append([i,j])
            
print(find_destroy(chicken_house))
