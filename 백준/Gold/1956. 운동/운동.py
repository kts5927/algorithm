import sys

input = sys.stdin.readline
def sol():
    n,m = map(int,input().split())
    graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = float('inf')

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = c

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    ans = float('inf')
    for i in range(1,n+1):
        ans = min(ans,graph[i][i])

    if ans != float('inf'):
        print(ans)
    else:
        print(-1)
sol()