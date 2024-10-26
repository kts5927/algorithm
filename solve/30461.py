import sys

N,M,Q = map(int,sys.stdin.readline().split())

fish = []
for i in range(N):
    fish.append(list(map(int,sys.stdin.readline().split())))


for i in range(1,N):
    for j in range(M):
        fish[i][j] += fish[i-1][j]

for i in range(1,N):
    for j in range(1,M):
        fish[i][j] += fish[i-1][j-1]
        
for i in range(Q):
    a , b = map(int,sys.stdin.readline().split())
    print(fish[a-1][b-1])