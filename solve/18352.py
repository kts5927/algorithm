import sys
from collections import deque
N,M,K,X = map(int,sys.stdin.readline().split())
node = [[] for _ in range(N+1)]
distance = [0 for _ in range(N+1)]
seq = deque([X])
distance[X] = 1
for i in range(M):
    a , b = map(int,sys.stdin.readline().split())
    node[a].append(b)
ans = []
while True:
    if seq :
        t = seq.popleft()
        for i in node[t]:
            if distance[i] == 0:
                distance[i] = distance[t]+1
                seq.append(i)
                if distance[i] == K+1:
                    ans.append(i)
    else : break
ans.sort()
if len(ans) == 0 :
    print('-1')

else:
    for i in ans:
        print(i)