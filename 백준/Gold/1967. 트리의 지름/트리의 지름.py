import sys
sys.setrecursionlimit(100000)

def dfs(node, dist):
    global Max, cal
    visited[node] = True
    
    if dist > Max:
        Max = dist
        cal = node
    
    for next_node, weight in tree[node]:
        if not visited[next_node]:
            dfs(next_node, dist + weight)

n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, w = map(int, sys.stdin.readline().split())
    tree[a].append((b, w))
    tree[b].append((a, w))

visited = [False] * (n + 1)
Max = 0
cal = 1
dfs(1, 0)

visited = [False] * (n + 1)
Max = 0
dfs(cal, 0)

print(Max)
