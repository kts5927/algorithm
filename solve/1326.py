import sys
from collections import deque
N = int(sys.stdin.readline())
bridge = list(map(int,sys.stdin.readline().split()))
start , end = map(int,sys.stdin.readline().split())
visit = [False  for _ in range(N+1)]
visit[start - 1] =True

jump = deque()
jump.append([start - 1 , 0])

while jump:
    a , b = jump.popleft()
    
    if a == end-1:
        print(b)
        sys.exit()
        
        
    for i in range(N):
        if not visit[i] and abs(i-a) % bridge[a] == 0:
            jump.append([i , b+1])
            visit[i] = True
            
print(-1)