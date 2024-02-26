import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


G = int(sys.stdin.readline().strip())
P = int(sys.stdin.readline().strip())

parent = [i for i in range(G + 1)]

count = 0
for _ in range(P):
    gi = int(sys.stdin.readline().strip())
    root = find_parent(parent, gi)
    if root == 0:
        break
    union_parent(parent, root, root - 1)
    count += 1

print(count)