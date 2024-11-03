import sys
import heapq

N , M = map(int,sys.stdin.readline().split())
Heap = []
for i in list(map(int,sys.stdin.readline().split())):
    heapq.heappush(Heap,-i)
kid = list(map(int,sys.stdin.readline().split()))

for i in kid:    
    a = -1 * heapq.heappop(Heap)
    if a < i:
        print(0)
        exit(0)

    a -= i
    if a > 0:
        heapq.heappush(Heap,-a)
print(1)