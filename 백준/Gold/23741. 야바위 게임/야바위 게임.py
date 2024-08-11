import sys
from collections import deque

N, M, X, Y = map(int, sys.stdin.readline().split())
lst = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    lst[a].append(b)
    lst[b].append(a)

dp = [[0] * (N + 1) for _ in range(Y + 1)]
location = deque()
visited_even = [False] * (N + 1)
visited_odd = [False] * (N + 1)

for i in lst[X]:
    location.append([i, 1])
    visited_even[i] = True

while location:
    e, t = location.popleft()
    if t > Y:
        break
    dp[t][e] += 1

    for i in lst[e]:
        if t % 2 == 1:
            if not visited_odd[i] and t <= Y:
                location.append([i, t + 1])
                visited_odd[i] = True
        else:
            if not visited_even[i] and t <= Y:
                location.append([i, t + 1])
                visited_even[i] = True

ans = []
if Y % 2 == 0:
    if not any(visited_odd):
        print(-1)
    else:
        for i in range(1, N + 1):
            if visited_odd[i]:
                ans.append(i)
        print(*ans)
else:
    if not any(visited_even):
        print(-1)
    else:
        for i in range(1, N + 1):
            if visited_even[i]:
                ans.append(i)
        print(*ans)
