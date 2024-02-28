from collections import deque

N = int(input())

while N:
    A, B = map(int, input().split())
    visited = set() 
    queue = deque([(A, "")]) 

    while queue:
        current, path = queue.popleft()
        
        if current == B:
            print(path)
            break
        
        if current not in visited:
            visited.add(current)
            queue.append((current * 2 % 10000, path + "D"))
            queue.append(((current - 1) % 10000, path + "S"))
            queue.append((current % 1000 * 10 + current // 1000, path + "L"))
            queue.append((current % 10 * 1000 + current // 10, path + "R"))

    N -= 1
