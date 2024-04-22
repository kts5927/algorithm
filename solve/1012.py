from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]



T = int(input())

for _ in range(T):
    
    M , N , K = map(int,input().split())
    field = [[0 for q in range(M)]for w in range(N)]
    ans = 0
    
    
    for p in range(K):
        X,Y = map(int,input().split())
        field[Y][X] = 1
    
    for i in range(N):
        for j in range(M):
            
            if field[i][j] == 1:
                seq = deque()
                seq.append([i,j])
                field[i][j] = 0
                while seq:
                    i_o,j_o = seq.popleft()
                    
                    for t in range(4):
                        y = i_o + dx[t]
                        x = j_o + dy[t]
                        
                        if 0 <= x < M and 0 <= y < N and field[y][x] == 1:
                            field[y][x] = 0
                            seq.append([y,x])
                                
                ans += 1
    print(ans)
                                    

    
    