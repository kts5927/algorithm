import heapq

strings = []

N = int(input())

for i in range(N):
    heapq.heappush(strings,-int(input()))
    
weight = 0
count = 1
ans = 0
for i in range(N):
    
    rope = -heapq.heappop(strings)
    
    if (count * rope) > weight:
        weight = count * rope
        ans = rope * count
    count += 1
    
print(ans)

