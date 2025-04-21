import sys
input = sys.stdin.readline

def sol():  
    N,M = map(int,input().split())

    DP = [[0] * (N+1)]
    for i in range(N):
        lst = list(map(int,input().split()))
        DP.append([0] + lst)


    for i in range(1,N+1):
        for j in range(1,N+1):
            DP[i][j] += DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1]


    for i in range(M):
        x1,y1,x2,y2 = map(int,input().split())
        print(DP[x2][y2] - DP[x1-1][y2] - DP[x2][y1-1] + DP[x1-1][y1-1])
sol()