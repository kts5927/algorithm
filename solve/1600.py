import sys
from collections import deque                
K = int(sys.stdin.readline())
W , H = map(int,sys.stdin.readline().split())
world = [list(map(int,sys.stdin.readline().split())) for _ in range(H)]
shadow = [[[float('inf') for i in range(W)] for j in range(H)] for k in range(K+1)]
shadow[K][0][0] = 0


seq= deque()
seq.append([0,0,K])
dxm = [1,-1,0,0] 
dym = [0,0,1,-1]

dxj = [2,2,1,1,-1,-1,-2,-2]
dyj = [1,-1,2,-2,2,-2,1,-1]

while seq:
    i , j , jump = seq.popleft()
    if i == H-1 and j == W-1:
        print(shadow[jump][i][j])
        sys.exit()
    for num in range(4):
        x = dxm[num] + i
        y = dym[num] + j
        if 0 <= x < H and 0 <= y < W and world[x][y] == 0 and shadow[jump][x][y] > shadow[jump][i][j] + 1:
            shadow[jump][x][y] = shadow[jump][i][j] + 1
            if x == H-1 and y == W-1:
                print(shadow[jump][x][y])
                sys.exit() 
            seq.append([x,y,jump])
    if jump >0:        
        for num in range(8):
            x = dxj[num] + i
            y = dyj[num] + j
            if 0 <= x < H and 0 <= y < W and world[x][y] == 0 and shadow[jump-1][x][y] > shadow[jump][i][j] + 1:
                shadow[jump-1][x][y] = shadow[jump][i][j] + 1
                if x == H-1 and y == W-1:
                    print(shadow[jump-1][x][y])
                    sys.exit() 
                seq.append([x,y,jump-1])
print(-1)
