import sys

def bellmans ():
    distance = [1e9]*(N+1)
    for i in range(N):
        for s,d,w in node:
            if distance[d] > distance[s] + w:
                distance[d] = distance[s] + w
                if i == N-1:
                    return 'YES'
    return 'NO'



TC = int(sys.stdin.readline())

for q in range(TC):
    N , M , W = map(int,sys.stdin.readline().split())
    node = []
    for k in range(M):
        a , b , c = map(int,sys.stdin.readline().split())
        node.append((a,b,c))
        node.append((b,a,c))
    for k in range(W):
        a , b , c = map(int,sys.stdin.readline().split())
        node.append((a,b,-c))

    print(bellmans())