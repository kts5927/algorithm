from collections import deque

N , M = map(int,input().split())

que = deque()
que.append(N)
visited = [0]*100001
method = 0
while que:
    q = que.popleft()
    
    if q == M:
        method += 1
        continue
        
    for i in q+1,q-1,q*2:
        if 0 <= i <= 100000:
            if visited[i] == 0:
                visited[i] = visited[q]+1
                que.append(i)
            elif visited[i]  == visited[q]+1:
                que.append(i)
        
print(visited[M])
print(method)
        
