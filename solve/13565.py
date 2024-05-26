from collections import deque

N , M = map(int,input().split())
lst = [list(map(int,input().strip())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = False
for i in range(M):
    if lst[0][i] == 0:
        cal = deque()
        cal.append([0,i])
        lst[0][i] = 1
        while cal:
            raw, colum = cal.popleft()

            for j in range(4):
                x = colum + dx[j]
                y = raw + dy[j]
                if 0<=x<M and 0<=y<N and lst[y][x] == 0:
                    if y == N-1:
                        ans = True
                        break
                    cal.append([y,x])
                    lst[y][x] = 1

        if ans:
            break

if ans:
    print('YES')
else:
    print('NO')