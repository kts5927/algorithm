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
    


  
# def find_entry(h : int , w : int , key:set , building : list , score):
#     lis = deque()
#     for i in range(h):
#         if building[i][0] == '.':
#             lis.append([i , 0])
#         if building[i][0].lower() in key or building[i][0] == '$':
#             lis.append([i , 0])
#             building[i][0] = '.'
#             score += 1
#         if ord('a') <= ord(building[i][0]) <= ord('z'):
#             lis.append([i , 0])
#             key.add(building[i][0])
#             building[i][0] = '.'
            
#         if building[i][w-1] == '.':
#             lis.append([i , w-1])
#         if building[i][w-1].lower() in key or building[i][w-1] == '$':
#             lis.append([i , w-1])
#             building[i][w-1] = '.'
#             score += 1
#         if ord('a') <= ord(building[i][w-1]) <= ord('z'):
#             lis.append([i , w-1])
#             key.add(building[i][w-1])
#             building[i][w-1] = '.'   
        
#     for i in range(w):
#         if building[0][i] == '.':
#             lis.append([0 , i])
#         if building[0][i].lower() in key or building[0][i] == '$':
#             lis.append([0 , i])
#             building[0][i] = '.'
#             score += 1
#         if ord('a') <= ord(building[0][i]) <= ord('z'):
#             lis.append([0 , i])
#             key.add(building[0][i])
#             building[0][i] = '.'    
            
#         if building[h-1][i] == '.':
#             lis.append([h-1 , i])
#         if building[h-1][i].lower() in key or building[h-1][i] == '$':
#             lis.append([h-1 , i])
#             building[h-1][i] = '.'
#             score += 1
#         if ord('a') <= ord(building[h-1][i]) <= ord('z'):
#             lis.append([h-1 , i])
#             key.add(building[h-1][i])
#             building[h-1][i] = '.' 
    
#     return lis , score
