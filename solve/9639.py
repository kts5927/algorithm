# import sys
# input = sys.stdin.readline


# T = int(input())

# for k in range(T):
#     N , M = map(int,input().split())
    
    
#     Rectangle = [list(map(int,input().split())) for _ in range(N)]
#     N_cal = [[0 for _ in range(M)] for _ in range(N)]
#     M_cal = [[0 for _ in range(M)] for _ in range(N)]
#     cal = [[0 for _ in range(M)] for _ in range(N)]
    
#     for i in range(M):
#         N_cal[N-1][i] = Rectangle[N-1][i]
    
#     for i in range(N-2,-1,-1):
#         for j in range(M):
#             N_cal[i][j] = N_cal[i+1][j] + Rectangle[i][j]
    
#     for i in range(N):
#         M_cal[i][M-1] = Rectangle[i][M-1]
    
#     for i in range(M-2,-1,-1):
#         for j in range(N):
#             M_cal[j][i] = M_cal[j][i+1] + Rectangle[j][i]
    
#     for i in N_cal:
#         print(i)
    
#     for i in M_cal:
#         print(i)
        
    

#     for i in range(N-1, -1, -1):
#         for j in range(M-1,-1,-1):
            
#             cal[i][j] = N_cal[i][j] + M_cal[i][j] - Rectangle[i][j]
#             if i < N-1 and j < M-1:
#                 cal[i][j] += cal[i+1][j+1]
            
#     Max = -float("inf")
    
#     for i in cal:
#         Max = max(Max,max(i))
        
#     print(Max)

## 비효율적인 방법 -> 3번 중첩계산

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    Rectangle = [list(map(int, input().split())) for _ in range(N)]

    cal = [[0] * M for _ in range(N)]

    for i in range(N - 1, -1, -1):
        for j in range(M - 1, -1, -1):
            down = cal[i + 1][j] if i + 1 < N else 0
            right = cal[i][j + 1] if j + 1 < M else 0
            diag = cal[i + 1][j + 1] if i + 1 < N and j + 1 < M else 0

            cal[i][j] = Rectangle[i][j] + down + right - diag

    result = max(max(row) for row in cal)
    print(result)
    
## 배열 하나에서 다 끝냄