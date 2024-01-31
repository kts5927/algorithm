import sys
from collections import deque

def find_farthest_node(start):
    visited = [False] * (V + 1)
    distance = [0] * (V + 1)
    queue = deque([(start, 0)]) 
    max_distance = 0
    farthest_node = 0

    while queue:
        node, dist = queue.popleft()
        visited[node] = True

        for neighbor, edge_dist in tree[node]:
            if not visited[neighbor]:
                new_dist = dist + edge_dist
                distance[neighbor] = new_dist
                queue.append((neighbor, new_dist))
                if new_dist > max_distance:
                    max_distance = new_dist
                    farthest_node = neighbor

    return farthest_node, max_distance

V = int(input())
tree = [[] for _ in range(V + 1)]

for _ in range(V):
    data = list(map(int, sys.stdin.readline().split()))
    node = data[0]
    for i in range(1, len(data), 2):
        if data[i] == -1:
            break
        neighbor = data[i]
        dist = data[i + 1]
        tree[node].append((neighbor, dist))

farthest_node, _ = find_farthest_node(1)

_, diameter = find_farthest_node(farthest_node)

print(diameter)