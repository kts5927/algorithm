from collections import deque
import sys
input = sys.stdin.readline

def bfs(F, S, G, U, D):
    queue = deque([(S, 0)])  
    visited = set([S]) 

    while queue:
        current, count = queue.popleft()

        if current == G:
            print(count)
            return
        
        if current + U <= F and (current + U) not in visited:
            queue.append((current + U, count + 1))
            visited.add(current + U)

        if current - D >= 1 and (current - D) not in visited:
            queue.append((current - D, count + 1))
            visited.add(current - D)
    
    print("use the stairs") 

F, S, G, U, D = map(int, input().split())

bfs(F, S, G, U, D)
