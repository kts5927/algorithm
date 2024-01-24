import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
edge = deque()
back = deque()
for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    edge.append([a,b,c])
    back.append([b,a,c])
start,end = map(int,sys.stdin.readline().split())

village = [0 for _ in range(n+1)]

while True:
    
    v,w,cost = edge.popleft()
    village[w] = max(village[w] , village[v]+cost)
    if len(edge) == 0:
        break
print(village[end])
count = 0
road = []
road.append(end)
while True:
    v,w,cost = back.pop()
    if village[w] == village[v] - cost and v in road:
        road.append(w)
        count+=1
    if len(back) == 0:
        break 
print(count)