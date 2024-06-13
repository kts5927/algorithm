import sys
from collections import deque
N , K = map(int,input().split())
ans = float('inf')
length = 0
rainbow_1 = [0]*K
rainbow_2 = [0]*K
deq = deque()
lst_1 = []
lst_2 = []
for i in range(N):
    a = int(sys.stdin.readline())
    rainbow_1[a-1] += 1
    lst_2.append(a)

for i in lst_2:
    rainbow_1[i-1] -= 1
    rainbow_2[i-1] += 1
    deq.append(i)
    length += 1
    while deq and rainbow_2[deq[0]-1] > 1:
        a = deq.popleft()
        rainbow_1[a-1] += 1
        rainbow_2[a-1]-=1
        length -= 1
    if 0 not in rainbow_1 and 0 not in rainbow_2:
        ans = min(ans,length)
        
if ans != float('inf'):
    print(ans)
else:
    print(0)
