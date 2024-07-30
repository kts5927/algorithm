import sys
import heapq
N = int(sys.stdin.readline())

lst_down = []
lst_up = []

for i in range(N):
    a = int(sys.stdin.readline())
    
    if a != 0:
        if a > 0:
            heapq.heappush(lst_up,a)
        else:
            heapq.heappush(lst_down,-a)
            
    else:
        if len(lst_down) >0 and len(lst_up) > 0:
            if lst_down[0] > lst_up[0]:
                print('ans = ',heapq.heappop(lst_up))
            else:
                print('ans = ',-heapq.heappop(lst_down))
        
        elif len(lst_down) == 0 and len(lst_up) == 0:
            print('ans = ',0)
        
        elif len(lst_down) == 0:
            print('ans = ',heapq.heappop(lst_up))
        
        elif len(lst_up) == 0:
            print('ans = ',-heapq.heappop(lst_down))
            