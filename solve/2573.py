import sys
sys.setrecursionlimit(10**7)
def ocean(land, i, j, N, M):
    ghost = 0

  

def check(shadow, i, j, N, M):
    shadow[i][j] = 0
    
    if i > 0 and shadow[i-1][j] != 0:
        check(shadow, i - 1, j, N, M)
    if i < N-1 and shadow[i+1][j] != 0:
        check(shadow, i + 1, j, N, M)
    if j > 0 and shadow[i][j-1] != 0:    
        check(shadow, i, j - 1, N, M)
    if j < M-1 and shadow[i][j+1] != 0:
        check(shadow, i, j + 1, N, M)
        
N, M = map(int, sys.stdin.readline().split())
land = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
time = 0
while True:
    ghost = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if land[i][j] != 0:
                if i < N - 1 and land[i + 1][j] == 0:
                    ghost[i][j] += 1
                if i > 0 and land[i - 1][j] == 0:
                    ghost[i][j] += 1
                if j < M - 1 and land[i][j + 1] == 0:
                    ghost[i][j] += 1
                if j > 0 and land[i][j - 1] == 0:
                    ghost[i][j] += 1
    for i in range(N):
        for j in range(M):
            land[i][j] = max(0, land[i][j] - ghost[i][j])
    time += 1
    ans = 0
    shadow = [row[:] for row in land]
    for i in range(N):
        for j in range(M):
            if shadow[i][j] != 0 :
                check(shadow, i, j, N, M)
                ans += 1
                if ans>1 : 
                    break
    icebergs = sum(1 for i in range(N) for j in range(M) if land[i][j] != 0)
    if icebergs == 0:
        time = 0
        break
    if ans >1 : 
        break
    if time == 0 or ans>1:
        break
   
print(time)
