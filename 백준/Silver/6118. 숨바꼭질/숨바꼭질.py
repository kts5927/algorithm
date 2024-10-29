from collections import deque

N , M = map(int,input().split())

node = [[] for _ in range(N+1)]
for i in range(M):
    a ,b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)
    
que = deque()
que.append(1)

dist = [0 for _ in range(N+1)]
dist[1] = 1

while que:
    location = que.popleft()

    for i in node[location]:
        if dist[i] == 0:
            que.append(i)
            dist[i] = dist[location] + 1

Max = max(dist)
dis = [i for i,d in enumerate(dist) if d == Max]
print(min(dis) , Max-1 , len(dis))