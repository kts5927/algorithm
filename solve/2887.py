# import sys
# N = int(sys.stdin.readline())
# x = []
# y = []
# z = []

# for i in range(1,N+1):
#   dx , dy , dz = map(int,sys.stdin.readline().split())
#   x.append([i , dx])
#   y.append([i , dy])
#   z.append([i , dz])

# x.sort(key = lambda x : x[1])
# y.sort(key = lambda y : y[1])
# z.sort(key = lambda z : z[1])

# planet = []

# for i in range(1 , N):
#     planet.append([x[i-1][0] , x[i][0] , (x[i][1] - x[i-1][1])])
#     planet.append([y[i-1][0] , y[i][0] , (y[i][1] - y[i-1][1])])
#     planet.append([z[i-1][0] , z[i][0] , (z[i][1] - z[i-1][1])])
    
# planet.sort(key = lambda  x : abs(x[2]))

# union = []
# for i in range(N+1):
#     union.append(i)

# ans = 0
# count = 0

# for i in planet:
#     cnt = False
#     if count == N:
#         break
#     if union[i[0]] != union[i[1]]:
#         ans += abs(i[2])
#         for j in range(1,N+1):
#             if union[j] == union[i[1]]:
#                 union[j] = union[i[0]]
#                 cnt = True
#     if cnt:
#         count +=1
                

# print(ans)

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
    count = 0
    for edge in edges:
        u, v, cost = edge
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            total_cost += cost
            if count == N:
                return total_cost
            else:count+=1

    return total_cost

N = int(sys.stdin.readline())
planets = []

for i in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    planets.append((x, y, z, i))

edges = []
print(kruskal(N, planets))
