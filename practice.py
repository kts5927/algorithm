# 백준 111 제목 티어 https://www.acmicpc.net/problem/

# 1562
# 1019
# 1006 <- 어려움
# https://www.acmicpc.net/problem/16953 그리디
import sys
from collections import deque

N = int(sys.stdin.readline())
dx = [1 , -1 , 0 , 0]
dy = [0 , 0 , 1 , -1]

for _ in range(N):
    h , w = map(int,sys.stdin.readline().split())
    building = []
    building = [['.'] + list(sys.stdin.readline().strip()) + ['.'] for _ in range(h)]
    building.insert(0, ['.'] * (w + 2))
    building.append(['.'] * (w + 2))
    key = {}
    for i in input():
        if i.isalpha():
            key[i] = True
    lst = []
    score = 0
    while True:
        diff = 0
        # lis , score = find_entry(h , w , key , building , score)
        lis = deque()
        lis.append([0,0])
        shadow = [[False for k in range(w+2)] for k in range(h+2)]
        door = []
        to_list = False    


        while lis : 
            i , j = lis.popleft()
            for k in range(4):
                if to_list :
                    break
                x = dx[k] + j
                y = dy[k] + i
                
                if 0 <= x < w+2 and 0 <= y < h+2 and building[y][x] != '*' and not shadow[y][x]:
                    if building[y][x] == '$':
                        building[y][x] = '.'
                        score += 1
                        lis.append([y , x])
                        shadow[y][x] = True
                        diff += 1
                        
                    elif building[y][x] == '.':
                        lis.append([y , x])
                        shadow[i][j] = True


                    elif ord('A') <= ord(building[y][x]) <= ord('Z'):
                        if building[y][x].lower() in key:
                            building[y][x] = '.'
                            lis.append([y , x])
                            shadow[y][x] = True
                            diff += 1
                        else:
                            door.append([y , x])
                        
                    elif ord('a') <= ord(building[y][x]) <= ord('z'):
                        key[building[y][x]] = True
                        building[y][x] = '.'
                        lis.append([y , x])
                        shadow[y][x] = True
                        for q in door:
                            if building[q[0]][q[1]].lower() in key:
                                building[q[0]][q[1]] = '.'
                                lis.append([q[0] , q[1]])
                                shadow[q[0]][q[1]] = True
                        diff += 1

        if diff == 0:
            break
        
    # print(key)
    print(score)