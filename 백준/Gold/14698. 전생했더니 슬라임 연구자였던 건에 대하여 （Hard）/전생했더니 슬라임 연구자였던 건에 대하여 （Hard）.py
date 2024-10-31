import heapq
import sys
T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    lst = list(map(int,sys.stdin.readline().split()))
    heap = []
    for j in lst:
        heapq.heappush(heap,j)
    cal = 1

    for i in range(N-1):
        slime = heapq.heappop(heap) * heapq.heappop(heap)
        cal *= slime
        cal %= 1000000007
        heapq.heappush(heap,slime)

    print(cal)