import heapq
import sys


K , N = map(int,sys.stdin.readline().split())
prime = list(map(int,sys.stdin.readline().split()))
que = []
for i in prime:
    heapq.heappush(que,i)

count = 0
while count < N:
    a = heapq.heappop(que)
    for i in prime:
        heapq.heappush(que,i*a)
        if a%i == 0:
            break
    count += 1
    

print(a)
