import sys
import heapq

N = int(sys.stdin.readline())
level = list(map(int,sys.stdin.readline().split())) 
Str = list(map(int,sys.stdin.readline().split()))
Day = int(sys.stdin.readline())

cal = [[0]*len(level) for _ in range(len(level)-1)]

for i in range(len(cal)):
    for j in range(len(cal[0])):
        if j > i:
            cal[i][j-i] = (Str[j]-Str[i]) / (j-i)
for i in cal:
    print(*i)
heap = []
for i in range(len(cal)):
    for j in range(len(cal[0])):
        if cal[i][j] > 0:
            heapq.heappush(heap,[-cal[i][j],i,j])

while heap:
    value, s, e = heapq.heappop(heap)
    print(s,e)
    if level[s] != 0:
        mx = min(Day//e , level[s])
        level[s] -= mx
        level[s+e] += mx
        Day -= mx*e
    
    if Day == 0:
        break
ans = 0
for i in range(len(level)):
    ans += level[i]*Str[i]
    
print(ans)