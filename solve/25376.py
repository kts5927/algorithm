import sys
from collections import deque

N = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))
on_off = [[] for _ in range(N)]  # Changed to N instead of N+1

for i in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    if arr[0] != 0:
        for j in range(arr[0]):
            on_off[i].append(arr[j+1])

ans = (1 << N) - 1
ans_list = []
bit = 0

for i in range(N):
    bit |= (switch[i] << i)

seq = deque()
seq.append((bit, 0))
last = set([bit])

while seq:
    bit, count = seq.popleft()

    if bit == ans:
        ans_list.append((count,bit))

    for i in range(N):
        if not bit & (1 << i):
            new_bit = bit | (1 << i) 
            if on_off[i]:  
                for j in on_off[i]:
                    new_bit ^= (1 << (j - 1)) 

            if new_bit not in last:
                last.add(new_bit)
                seq.append((new_bit, count + 1))
if ans_list:
    print(ans_list[0][0])
else : print(-1)