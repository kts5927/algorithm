import sys
import heapq

T = int(sys.stdin.readline())
for i in range(T):
    M = int(sys.stdin.readline())

    lst = []
    while len(lst) != M:
        dummy = list(map(int,sys.stdin.readline().split()))
        for input in dummy:
            lst.append(input)
    
    left_lst = []
    left_len = 0
    right_lst = []
    right_len = 0
    ans = []
    for number in range(len(lst)):
        
        if left_len > 0 and right_len > 0:
            if lst[number] < -left_lst[0]:
                heapq.heappush(left_lst,-lst[number])
                left_len += 1
            else :
                heapq.heappush(right_lst, lst[number])
                right_len += 1
                
        
        else:
            if left_len == 0:
                heapq.heappush(left_lst,-lst[number])
                left_len += 1        
            elif right_len == 0:    
                heapq.heappush(right_lst,lst[number])
                right_len += 1
                
        while left_len > 0 and right_len > 0 and right_lst[0] + left_lst[0] < 0:
            heapq.heappush(right_lst, -heapq.heappop(left_lst))
            left_len -= 1
            right_len += 1
            
        
        while abs(left_len - right_len) > 1:
            if left_len > right_len:
                heapq.heappush(right_lst,-heapq.heappop(left_lst))
                left_len -= 1
                right_len += 1
            if left_len < right_len:
                heapq.heappush(left_lst,-heapq.heappop(right_lst))
                left_len += 1
                right_len -= 1
                
        if number%2 == 0:
            if left_len > right_len:
                ans.append(-left_lst[0])
            if left_len < right_len:
                ans.append(right_lst[0])

    print(len(ans))
    print(*ans)