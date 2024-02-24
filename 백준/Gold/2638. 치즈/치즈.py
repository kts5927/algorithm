from collections import deque
import sys

N,M=map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def bfs(arr):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    count = 0
    lista = deque()
    
    while True:
        lista.append((0,0))
        while lista:
            i,j = lista.popleft()
            if arr[i][j] == 0:
                arr[i][j] = 2
                for _ in range(4):
                    x = dx[_] + i
                    y = dy[_] + j
                    if -1 < x < N and -1 < y < M and arr[x][y] == 0 :
                        lista.append((x,y))


        for i in range(N):
            for j in range(M):
                
                if arr[i][j] == 1:
                    number = 4
                    for _ in range(4):
                        x = dx[_] + i
                        y = dy[_] + j
                        if arr[x][y] ==2:
                            number -= 1
                    if number <= 2:
                        arr[i][j] = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 2:
                    arr[i][j] = 0
        count += 1 
        if sum(sum(row) for row in arr) == 0:
            print(count)
            break
   
bfs(arr)                