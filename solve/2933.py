import sys
from collections import deque

N , M = map(int,input().split())
lst = [list(map(str,sys.stdin.readline().strip())) for _ in range(N)]
T = int(input())
stick = list(map(int,sys.stdin.readline().split()))
is_odd = True

for i in stick:
    que = deque()
    
    if is_odd:
        for j in range(len(lst[N-i])):
            if lst[N-i][j] == 'x':
                lst[N-i][j] = '.'
                que.append([N-i,j])
                is_odd = False
                break
    else:
        for j in range(len(lst[N-i])-1,0,-1):
            if lst[N-i][j] == 'x':
                lst[N-i][j] = '.'
                que.append([N-i,j])
                is_odd = True
                break
    
    
    
    
    
    
print(que)
                