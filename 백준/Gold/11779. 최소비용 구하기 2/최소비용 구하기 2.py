import sys
from collections import deque
import copy
n = int(input())
m = int(input())

city = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
trip = [[] for _ in range(n+1)]
cost = [n * 100001 for _ in range(n+1)]
node = [0 for _ in range(n+1)]


for i in range(m):
    a , b , c = map(int,sys.stdin.readline().split())
    city[a].append([b,c])
    node[b] += 1
start , end = map(int,input().split())


cost[start] = 0 
cal = deque()
cal.append((start , 0))
trip[start].append(start)

while cal:
    now , pay = cal.popleft()
    if(cost[now] < pay): continue
    for i in city[now]:
        if cost[i[0]] > cost[now] + i[1]: 
            cal.append((i[0] , i[1]))             
            cost[i[0]] = cost[now] + i[1]
            trip[i[0]] = copy.deepcopy(trip[now])
            trip[i[0]].append(i[0])



print(cost[end])
print(len(trip[end]))
print(*trip[end])
