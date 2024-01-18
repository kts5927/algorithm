import sys
import heapq


right_heap = []
left_heap = []

#만약 전체 개수가 0개라면 = 왼쪽에 넣음
#항상 왼/오가 같거나
#왼쪽이 1개 더 많게.
count = 0
N = int(sys.stdin.readline())
for i in range(N):
    number = int(sys.stdin.readline())
    
    
    if len(left_heap) == 0: 
        heapq.heappush(left_heap,(-1)*number)
    elif -1*left_heap[0] >= number : 
        heapq.heappush(left_heap,(-1)*number)
    else :
        heapq.heappush(right_heap,number)
    
    
        
    if len(right_heap)>len(left_heap):
        remove = heapq.heappop(right_heap)
        heapq.heappush(left_heap,(-1)*remove)
        
        
    elif len(left_heap)-len(right_heap)>=2 : 
        remove = -heapq.heappop(left_heap)
        heapq.heappush(right_heap,remove)
    
    
    
    print((-1)*left_heap[0])
  
  
  
  
