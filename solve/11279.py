import sys
import heapq

heap = []
n = int(input())
for i in range(n):
    n1 = int(sys.stdin.readline())
    if n1 == 0:
        if heap:
            print((-1)*heapq.heappop(heap))
        else : 
            print(0)
    else : 
        heapq.heappush(heap,(-1)*n1)
        
