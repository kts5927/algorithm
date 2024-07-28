import heapq
import sys

N = int(sys.stdin.readline())
lst = []

for i in range(N):
    a = int(sys.stdin.readline())
    if a != 0:
        heapq.heappush(lst,a)
        
    else:
        if len(lst) == 0:
            print(0)
        else:
            print(lst[0])
            heapq.heappop(lst)
