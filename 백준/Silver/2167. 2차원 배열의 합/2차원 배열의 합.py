N,M = map(int,input().split())
array = []
for i in range(N):
    array.append(list(map(int,input().split())))

cum = [[0]*(M+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,M+1):
        cum[i][j] = cum[i-1][j] + cum[i][j-1] + array[i-1][j-1] - cum[i-1][j-1]

T = int(input())

for _ in range(T):
    i,j,x,y = map(int,input().split())
    ans = cum[x][y] - cum[x][j-1] - cum[i-1][y] + cum[i-1][j-1]
    print(ans)