import sys
sys.setrecursionlimit(10**7)
N,M = map(int,sys.stdin.readline().split())
lists = [[] for i in range(N+1)]
visit = [False for i in range(N+1)]
count = 0
for i in range(M):
    u,v = map(int,sys.stdin.readline().split())
    lists[u] += [v]
    lists[v] += [u]

def check(i):
    if not visit[i] : 
        visit[i] = True
        for j in range(len(lists[i])):
            check(lists[i][j])

for i in range(1,N+1):
    if not visit[i]:
        count+=1
        check(i)
        
print(count)

