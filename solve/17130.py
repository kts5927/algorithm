import sys
N , M = map(int,sys.stdin.readline().split())

world = [sys.stdin.readline().strip() for _ in range(N)]
shadow = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

for j in range(M):
    for i in range(N):

        if(world[i][j] == "R" and j < M-1):
            if(i != 0 ):
                visited[i-1][j+1] = True
            if(i != N-1):
                visited[i+1][j+1] = True
                
            visited[i][j+1] = True

        if(world[i][j] == "C" and visited[i][j] and j < M-1):
            if(i != 0 ):
                visited[i-1][j+1] = True
                shadow[i-1][j+1] = max(shadow[i][j]+1 , shadow[i-1][j+1])
            if(i != N-1 ):
                visited[i+1][j+1] = True
                shadow[i+1][j+1] = max(shadow[i][j]+1 , shadow[i+1][j+1])

            visited[i][j+1] = True
            shadow[i][j+1] = max(shadow[i][j]+1 , shadow[i][j+1])

        if((world[i][j] == "." or world[i][j] == "O") and visited[i][j] and j < M-1 ):
            if(i != 0):
                visited[i-1][j+1] = True
                shadow[i-1][j+1] = max(shadow[i][j] , shadow[i-1][j+1])
            if(i != N-1):
                visited[i+1][j+1] = True
                shadow[i+1][j+1] = max(shadow[i][j] , shadow[i+1][j+1])
                
            visited[i][j+1] = True
            shadow[i][j+1] = max(shadow[i][j] , shadow[i][j+1])

ans = []
for i in range(N):
    for j in range(M):
        if(world[i][j] == "O" and visited[i][j]):
            ans.append(shadow[i][j])


if(len(ans) == 0):
    print(-1)
else:
    print(max(ans))
    
