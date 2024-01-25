import sys
N , K = map(int,sys.stdin.readline().split())
arr = []
for i in range(N):
    a , b = map(int,sys.stdin.readline().split())
    arr.append([a,b])


table = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        if arr[i-1][0] <= j:
            table[i][j] = max(table[i-1][j], table[i-1][j-arr[i-1][0]] + arr[i-1][1])
            
        else : table[i][j] = table[i-1][j]
            

print(table[-1][-1])