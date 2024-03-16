# 백준 111 제목 티어 https://www.acmicpc.net/problem/

# 1562
# 1019
# https://www.acmicpc.net/problem/16953 그리디


import sys
from collections import deque
N , M , K = map(int,sys.stdin.readline().split())
wall = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
shadow = [[[False for _ in range(M)] for _ in range(N)] for _ in range(K)]
location = deque()
location.append([0 , 0 , 0 , 0])

dx = [1 , -1 , 0 , 0]
dy = [0 , 0 , 1 , -1]
while location:
    i , j , k , count= location.popleft()
    shadow[k][j][i] = True
    if i == M-1 and j == N-1:
        print(count)
        break	
	
    for a in range(4):
        x = dx[a] + i
        y = dy[a] + j
		
        if 0 <= x < M and 0 <= y < N and not shadow[k][y][x]:
            print(x , y , count , k)
            if wall[x][y] == 0 :
                location.append([x , y , k , count + 1 ])
			
            elif wall[x][y] == 1 and k < K-1:
                print('here!')
                location.append([x , y , k+1 , count + 1])