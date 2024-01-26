import sys
N = int(sys.stdin.readline())

Matrix = [list(map(int,sys.stdin.readline().split()))for _ in range(N)]

table = [[0 for _ in range(N)] for _ in range(N)]

for term in range(1,N):
    for start in range(N):
        if start + term == N:
            break
    
        table[start][start + term] = int(1e9)
        
        for t in range(start,start+term):
            table[start][start + term] = min(table[start][start+term],table[start][t] + table[t+1][start+term] + Matrix[start][0]*Matrix[t][1]*Matrix[start+term][1])
            
print(table[0][N-1])