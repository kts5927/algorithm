import sys
sys.setrecursionlimit(10**6)

def DFS(a):
    global count
    visited[a] = count
    count += 1
    for k in lst[a]:
        if visited[k] == 0:
            DFS(k)


N , M , R = map(int,sys.stdin.readline().split())
lst = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
count = 1
for i in range(M):
    u , v = map(int,sys.stdin.readline().split())
    lst[u].append(v)
    lst[v].append(u)
    
for i in lst:
    i.sort()
DFS(R)

for i in range(1,len(visited)):
 print(visited[i])

