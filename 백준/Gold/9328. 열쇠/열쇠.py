import sys
from collections import deque

N = int(sys.stdin.readline())
dx = [1 , -1 , 0 , 0]
dy = [0 , 0 , 1 , -1]

for _ in range(N):
    h , w = map(int,sys.stdin.readline().split())
    building = []
    building = ['.' + sys.stdin.readline() + '.' for _ in range(h)]
    building = ['.' * (w+2)] + building + ['.' * (w+2)]
    shadow = [[False for k in range(w+2)] for k in range(h+2)]
    key = {}
    visited_doc = []
    for i in input():
        if i.isalpha():
            key[i] = True
    score = 0
    lis = deque([[0 , 0]])
    shadow[0][0] = True


    while lis : 
        i , j = lis.popleft()
        for k in range(4):
            x = dx[k] + j
            y = dy[k] + i
            if x < 0 or x >= w+2 or y < 0 or y >= h+2 or building[y][x] == '*' or shadow[y][x]:
                continue
            if 'A' <= building[y][x] <= 'Z': 
                if building[y][x].lower() not in key: 
                    continue  
            elif 'a' <= building[y][x] <= 'z':
                if building[y][x] not in key: 
                    key[building[y][x]] = True  
                    shadow = [[False] * (w + 2) for _ in range(h + 2)] 
            elif building[y][x] == "$" and (y, x) not in visited_doc: 
                score += 1 
                visited_doc.append((y, x))  


            shadow[y][x] = True  
            lis.append([y, x]) 


    print(score)