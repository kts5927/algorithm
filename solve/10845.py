import sys
from collections import deque
N = int(sys.stdin.readline())
que = deque()

while N:
    a = list(map(str , sys.stdin.readline().split()))
    
    if a[0] == 'push':
        que.append(int(a[1]))
    elif a[0] == 'pop':
        if len(que):    
            print(que.popleft())
        else : print(-1) 
        
    elif a[0] == 'size':
        print(len(que))
    elif a[0] == 'empty':  
        if len(que):
            print(0)
        else :
            print(1)
    elif a[0] == 'front':
        if len(que):
            print(que[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if len(que):
            print(que[-1])
        else:
            print(-1)
    
    N -= 1