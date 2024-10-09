from collections import deque

def union(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = union(parent[x]) 
        return parent[x]

def merge(x, y):
    a = union(x)
    b = union(y)
    if a == b:
        return False 
    parent[b] = a
    return True

def check(start, visited):
    que = deque([(start, -1)]) 
    visited[start] = True
    cycle_check = True 
    
    while que:
        node, prev = que.popleft()
        for neighbor in tree[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                if not merge(node, neighbor): 
                    cycle_check = False
                que.append((neighbor, node)) 
            elif neighbor != prev:
                cycle_check = False

    return cycle_check

case_number = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    tree = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
        
    visited = [False] * (n + 1)
    parent = [i for i in range(n + 1)]  
    ans = 0 

    for i in range(1, n + 1):
        if not visited[i]: 
            if check(i, visited): 
                ans += 1

    if ans == 0:
        print(f'Case {case_number}: No trees.')
    elif ans == 1:
        print(f'Case {case_number}: There is one tree.')
    else:
        print(f'Case {case_number}: A forest of {ans} trees.')
    
    case_number += 1
