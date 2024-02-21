import sys
input = sys.stdin.readline

n = int(input())
node = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

parent = [0 for _ in range(n+1)]
visit = [False for _ in range(n+1)]
visit[1] = True
queue = [1]

while queue:
    current = queue.pop(0)
    for next_node in node[current]:
        if not visit[next_node]:
            parent[next_node] = current
            visit[next_node] = True
            queue.append(next_node)
queue = set
queue = list

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    ancestors_a = set()

    while a:
        ancestors_a.add(a)
        a = parent[a]
    
    while b not in ancestors_a:
        b = parent[b]
    
    print(b)