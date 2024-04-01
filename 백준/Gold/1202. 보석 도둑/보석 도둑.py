import sys
import heapq



N , K = map(int,sys.stdin.readline().split())
gem = []
for i in range(N):
    weight , value = map(int,sys.stdin.readline().split())
    gem.append([weight,value])
backpack = [int(sys.stdin.readline()) for _ in range(K)]
gem.sort()
backpack.sort()
n = 0
ans = 0
cal = []
for k in backpack:
    while n < N and k >= gem[n][0]:
        heapq.heappush(cal, -gem[n][1])
        n += 1
    if cal:
        ans += heapq.heappop(cal)


print(-ans)
