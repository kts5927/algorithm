import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N + 1)]
client = [0 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    client[b] += 1
    
for i in range(1, N + 1):
    arr[i].sort()
    

cal = []
ans = []

for i in range(1, N + 1):
    if client[i] == 0:
        heapq.heappush(cal, i)
        visited[i] = True



while cal:
    now = heapq.heappop(cal)
    ans.append(now)
    for j in arr[now]:
        client[j] -= 1
        if client[j] == 0 and not visited[j]:
            heapq.heappush(cal, j)
            visited[j] = True



print(*ans)
