import sys
from collections import deque
deq = deque()
N = int(input())

while N:
    a = list(map(str , sys.stdin.readline().split()))
    
    
    if a[0] == 'push_front':
        deq.insert(0 , int(a[1]))
    elif a[0] == 'push_back':
        deq.append(int(a[1]))
    elif a[0] == 'pop_front':
        if deq:
            print(deq.popleft())
        else :
            print(-1)
    elif a[0] == 'pop_back':
        if deq:
            print(deq.pop())
        else :
            print(-1)
    elif a[0] == 'size':
        print(len(deq))
    elif a[0] == 'empty':
        if len(deq):
            print(0)
        else:
            print(1)
    elif a[0] == 'front':
        if deq:
            print(deq[0])
        else : 
            print(-1)
    elif a[0] == 'back':
        if deq:
            print(deq[-1])
        else : 
            print(-1)
    N-=1