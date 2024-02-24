import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    else:
        parent[y_root] = x_root
        if rank[x_root] == rank[y_root]:
            rank[x_root] += 1

def kruskal(N, planets):
    parent = [i for i in range(N)]
    rank = [0] * N
    total_cost = 0

    for i in range(3):
        planets.sort(key=lambda x: x[i])
        prev = 0
        for j in range(1, N):
            cost = abs(planets[j][i] - planets[prev][i])
            prev = j
            edges.append((planets[j-1][3], planets[j][3], cost))

    edges.sort(key=lambda x: x[2])

    for edge in edges:
        u, v, cost = edge
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            total_cost += cost

    return total_cost

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    planets = []

    for i in range(N):
        x, y, z = map(int, sys.stdin.readline().split())
        planets.append((x, y, z, i))

    edges = []
    print(kruskal(N, planets))
