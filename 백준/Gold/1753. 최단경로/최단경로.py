import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
graph = [[] for _ in range(V + 1)]
weight = [float('inf') for _ in range(V + 1)]
weight[N] = 0
seq = []
visit = [False for _ in range(V + 1)]
check = V
heapq.heappush(seq, (0, N))

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

while seq:
    dist, node = heapq.heappop(seq)
    if visit[node] or weight[node] < dist:
        continue
    visit[node] = True
    check -= 1
    for w, v in graph[node]:
        if not visit[v]:
            if weight[v] > weight[node] + w:
                weight[v] = weight[node] + w
                heapq.heappush(seq, (weight[v], v))
    if check == 0:
        break

for i in range(1, V + 1):
    if weight[i] == float('inf'):
        print("INF")
    else:
        print(weight[i])
