import sys
from collections import deque

N,M,X,Y = map(int,sys.stdin.readline().split())
lst = [[] for _ in range(N+1)]
for i in range(M):
    a , b = map(int,sys.stdin.readline().split())
    lst[a].append(b)
    lst[b].append(a)
    
dp = [[0]*(N+1) for _ in range(Y+1)]
location = deque()
visited_even = []
visited_odd = []
for i in lst[X]:
    location.append([i,1])
    visited_even.append(i)
    
while location:
    e , t = location.popleft()
    if t > Y:
        break
    dp[t][e] += 1

    for i in lst[e]:
        if t%2 == 1:
            if i not in visited_odd and t <= Y:
                location.append([i,t+1])
                visited_odd.append(i)
        else:
            if i not in visited_even and t <= Y:
                location.append([i,t+1])
                visited_even.append(i)
               
ans = []
if Y%2 == 0:
    if len(visited_odd) == 0:
        print(-1)
    else:
        visited_odd.sort()
        for i in visited_odd:
            if i not in ans:
                ans.append(i)
        print(*ans)
else:
    if len(visited_even) == 0:
        print(-1)
    else:
        visited_even.sort()
        for i in visited_even:
            if i not in ans:
                ans.append(i)
        print(*ans)

