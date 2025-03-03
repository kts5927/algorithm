mod = 10**9+7  

di_down = [1,0,-1]
dj_down = [-1,-1,0]

di_up = [0,-1,-1]
dj_up = [-1,-1,0]

N,M = map(int,input().split())
K = int(input())
is_blink = [[False for _ in range(M+1)]for _ in range(M+N+1)]
for i in range(K):
    n,m = map(int,input().split())
    is_blink[n][m] = True
    
hive = [[0 for _ in range(M+1)]for _ in range(M+N+1)]
hive[1][1] = 1
for k in range(1,M+N+1):
    x = k
    y = 1
    
    check = True
    while  True:
        
        if 0 < x <= N   and 0 < y <= M and not is_blink[x][y]:
            for i in range(3):
                if not check:
                    I = x + di_down[i]
                    J = y + dj_down[i]
                else:
                    I = x + di_up[i]
                    J = y + dj_up[i]

                if 1 <= I and 1 <= J:
                    hive[x][y] += hive[I][J]
                    hive[x][y] %= mod
        if check:
            x -= 1
            y += 1
        else:
            y += 1

        check = not check
        if x == 0:
            break
        
print(hive[N][M])