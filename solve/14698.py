import heapq
T = int(input())

for i in range(T):
    N = int(input())
    lst = list(map(int,input().split()))
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