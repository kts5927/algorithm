from collections import deque

def solution():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    

    graph = [[] for _ in range(n + 1)]
    

    index = 2
    for _ in range(m):
        x = int(data[index])
        y = int(data[index + 1])
        graph[x].append(y)
        graph[y].append(x)
        index += 2
    
 
    def bfs(start):
        distances = [-1] * (n + 1) 
        queue = deque([start])
        distances[start] = 0 
        
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if distances[neighbor] == -1:  
                    queue.append(neighbor)
                    distances[neighbor] = distances[current] + 1 
        
        return distances
    
   
    distances = bfs(1)
    

    max_distance = max(distances)
    
   
    longDis= [i for i, d in enumerate(distances) if d == max_distance]
    

    longD = min(longDis)
    
   
    count_farthest = len(longDis)
    

    print(longD, max_distance, count_farthest)

solution()