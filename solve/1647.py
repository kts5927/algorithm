import sys
from collections import deque

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent , parent[x])
    return parent[x]

def cal(parent , start , end):
    A = find(parent , start)
    B = find(parent , end)
    
    if(A != B):
        parent[A] = B
    
N , M = map(int,sys.stdin.readline().split())
route = []

for _ in range(M):
    start , end , cost = map(int , sys.stdin.readline().split())
    route.append([cost , start , end])
    
parent = [i for i in range(N+1)]

route.sort()
route = deque(route)
c_sum = 0
last = 0
count = 0
while route:
    cost , start , end = route.popleft()
    if find(parent , start) != find(parent , end):
        last = cost
        c_sum += cost
        cal(parent , start , end)
        print(parent)
        if count == N-1:
            break
        else : 
            count += 1


            
print(c_sum - last)