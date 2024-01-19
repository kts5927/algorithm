import sys

def find(parents, x):
    if parents[x] == x:
        return x
    parents[x] = find(parents, parents[x])  # Path Compression
    return parents[x]

def union(parents, x, y):
    root_x = find(parents, x)
    root_y = find(parents, y)

    if root_x != root_y:
        parents[root_y] = root_x

V, E = map(int, sys.stdin.readline().split())
lists = []
parents = [i for i in range(V + 1)]

for i in range(E):
    parent, child, cost = map(int, sys.stdin.readline().split())
    lists.append([cost, parent, child])

lists.sort()
cost = 0

for i in range(E):
    if find(parents, lists[i][1]) != find(parents, lists[i][2]):
        cost += lists[i][0]
        union(parents, lists[i][1], lists[i][2])

print(cost)
