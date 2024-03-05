import sys
from collections import deque
N , M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a , b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

ans = [1 for _ in range(N)]
visit = [False for _ in range(N + 1)]
while True:
    lst = deque()
    for i in range(N):
        if not visit[i]:
            lst.append(i+1)
            count = 1
            while lst:
                a = lst.popleft()
                if visit[a] == False:
                    visit[a] = True
                    ans[a-1] = count
                count += 1
                for i in graph[a]:
                    if not visit[i]:
                        
                        lst.append(i)
    break

print(*ans )