import sys
sys.setrecursionlimit(10**7)
N= int(sys.stdin.readline())
lists = [[] for i in range(N+1)]
visit = [0 for i in range(N+1)]
count = 0
for i in range(N-1):
    u,v = map(int,sys.stdin.readline().split())
    lists[u] += [v]
    lists[v] += [u]
def check(i):
    for j in range(len(lists[i])):
        if visit[lists[i][j]] == 0:
            visit[lists[i][j]] = i
            check(lists[i][j])

check(1)

for i in range(2,len(visit)):
    print(visit[i])