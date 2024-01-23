import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]
count = [0 for _ in range(N+1)]

for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    count[b] += 1
    

visited = [False for _ in range(N+1)]
visited[0] = True
seq = deque()
ans = deque()
while visited.count(False) != 0:
    for i in range(1, N+1):
        if count[i] == 0 and visited[i]  == False:
            ans.append(i)
            seq.append(i) 
           
    for j in range(len(seq)):
        a = seq.popleft()
        for i in arr[a]:
            count[i] -= 1
        visited[a] = True
        
print(*ans)