import sys
from collections import deque

dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,1,-1,1,-1,1,-1]
ans = []


while True:
    N , M = map(int,input().split())
    if N == 0 and M == 0:
        break
    
    else:
        lst = [list(map(int,sys.stdin.readline().split()) )for _ in range(M)]
        count = 0
        for i in range(M):
            for j in range(N):

                if lst[i][j] == 1:
                    lst[i][j] = 0
                    cal = deque()
                    cal.append([i,j])
                    count += 1
                    while cal:
                        q,w = cal.popleft()
                        
                        for k in range(8):
                            y = q+dy[k]
                            x = w+dx[k]
                            
                            if 0 <= x < N and 0 <= y < M and lst[y][x] == 1:
                                lst[y][x] = 0
                                cal.append([y,x])
                    
        ans.append(count)
        

for i in ans:
    print(i)