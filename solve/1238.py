from collections import deque
N , M , X = map(int,input().split())

village = [[] for _ in range(N+1)]
for i in range(M):
    a , b , c = map(int,input().split())
    village[a].append([b,c])

def search(t , k):
    price = [float('inf') for _ in range(N+1)]
    price[t] = 0
    visited = [False for _ in range(N+1)]
    q = deque()
    q.append(t)
    while q:
        now = q.popleft()
        visited[now] = True
        for destination , cost in village[now]:
            if price[now] + cost < price[destination]:
                price[destination] = price[now] + cost
                q.append(destination)
    return price[k]

ans1 = []
ans2 = []
ans = []
for i in range(1 , N+1):
    ans1.append(search(i , X))
    ans2.append(search(X , i))
for i in range(N):
    ans.append(ans1[i] + ans2[i])
print(max(ans))
