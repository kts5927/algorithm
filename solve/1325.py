import sys
from collections import deque
input = sys.stdin.readline

def bfs(i):
    q = deque([i])
    v = [0] * (N+1)
    v[i] = 1
    vs = 1
    while q:
        a = q.popleft()
        for j in c[a]:
            if not v[j]:
                vs += 1
                v[j] = 1
                q.append(j)
    return vs

N , M = map(int,input().split())
c = [[] for _ in range(N+1)]
for i in range(M):
    A , B = map(int,input().split())
    c[B].append(A)
M = 1
ans = []
for i in range(1,N+1):
    vs = bfs(i)
    if M < vs:
        ans = []
        ans.append(i)
        M = vs
    elif M == vs:
        ans.append(i)
    
print(*ans)