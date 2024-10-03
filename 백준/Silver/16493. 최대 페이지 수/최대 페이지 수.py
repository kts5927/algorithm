import sys

N , M = map(int,sys.stdin.readline().split())

read = [[0 for _ in range(N+1)] for _ in range(M+1)]
for i in range(1,M+1):
    a , b = map(int,sys.stdin.readline().split())
    
    for j in range(1,N+1):
        if j-a >= 0:
            read[i][j] = max(read[i-1][j],0+read[i-1][j-a] + b)
        else:
            read[i][j] = read[i-1][j]

    
print(read[-1][-1])