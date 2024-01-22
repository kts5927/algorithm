import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
lists = [[] for _ in range(N + 1)]
costs = [float("inf")] * (N + 1)

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    lists[a].append((b, c))

start, end = map(int, sys.stdin.readline().split())

pq = [(start,0)]
costs[start] = 0
while pq:
    w,cost = heapq.heappop(pq)
    if cost > costs[w]:
        continue
    for a, b in lists[w]:
        if costs[a] > cost + b:
            costs[a] = cost + b
            heapq.heappush(pq, (a,costs[a]))

print(costs[end])
