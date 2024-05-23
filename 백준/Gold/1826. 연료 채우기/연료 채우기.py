import sys
import heapq

N = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
destination = list(map(int, sys.stdin.readline().split()))
fuel = destination[1]
fuel_lst = []
ans = 0

# 주유소 위치에 따라 정렬
lst.sort()

for i in lst:
    while i[0] > fuel:
        if len(fuel_lst) > 0:
            fuel -= heapq.heappop(fuel_lst)
            ans += 1
        else:
            ans = -1
            break
    if ans == -1:
        break
    heapq.heappush(fuel_lst, -i[1])

if ans != -1:
    while destination[0] > fuel:
        if len(fuel_lst) > 0:
            fuel -= heapq.heappop(fuel_lst)
            ans += 1
        else:
            ans = -1
            break
        
print(ans)
