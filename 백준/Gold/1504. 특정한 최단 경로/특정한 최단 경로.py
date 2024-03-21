import sys
import heapq


def dijkstra(v1 , v2):
    global ans
    deq = []
    heapq.heappush(deq , (0 ,v1))
    shadow = [float('inf') for _ in range(N+1)]
    shadow[v1] = 0

    while deq:
        cost , now = heapq.heappop(deq)
        if shadow[now] < cost:
            continue
        for i in node[now]:
            # print(shadow , i , now , cost)
            distance = shadow[now] + i[0]
            if distance < shadow[i[1]]:
                shadow[i[1]] = distance
                heapq.heappush(deq , (i[0] , i[1]))
    if shadow[v2] != float('inf'):         
        return shadow[v2]
        
    return shadow[v2]




N , E = map(int,sys.stdin.readline().split())
node = [[] for _ in range(N+1)]
for _ in range(E):
    a , b , c = map(int,sys.stdin.readline().split())
    node[a].append([c , b])
    node[b].append([c , a])

v1 , v2 = map(int,sys.stdin.readline().split())


# print(dijkstra(1 , v1))
# print(dijkstra(v1 , v2))
# print(dijkstra(v2 , N))
# print(dijkstra(1 , v2))
# print(dijkstra(v2 , v1))
# print(dijkstra(v1 , N))

ans =  min((dijkstra(1 , v1) + dijkstra(v1 , v2) + dijkstra(v2 , N)) , (dijkstra(1 , v2) + dijkstra(v2 , v1) + dijkstra(v1 , N)))

if ans == float('inf'):
    print(-1)
else : print(ans)
