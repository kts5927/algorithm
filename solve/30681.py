import sys
from collections import deque

def ccw(a,b,c):
    return (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])

def dest(a,b):
    return ((a[0] - b[0])**2 + (a[1]-b[1])**2)**0.5
    
def coordinate(a,b):
    return [b[0]-a[0] , b[1]-a[1]]


def isparallel(lst:list):
    n = len(lst)
    i = 0
    j = 1
    deq = deque()
    deq.append(dest(lst[i] , lst[i+1]))
    cal = deq[0]
    ans = 10000
    while i < n:
        if ccw(lst[i],coordinate(lst[(i+1)%n],lst[i]),coordinate(lst[(j+1)%n],lst[j])) >= 0 :
            if ccw(lst[i],coordinate(lst[(i+1)%n],lst[(i)%n]),coordinate(lst[(j+2)%n],lst[(j+1)%n])) < 0:
                i += 1
                ans = min(ans , cal)
                cal -= deq[0]
                deq.popleft()
            else:
                j+=1
                j %= n
                deq.append(dest(lst[j],lst[(j+1)%n]))
                cal += deq[-1]
            
            
    return ans
            
    
    

def convexhull(points:list):
    points.sort()
    n = len(points)
    up = []
    down = [] 
    up = []
    for i in range(n):
        while len(up) > 1 and ccw(up[-2],up[-1],points[i]) <= 0:
            up.pop()
        up.append(points[i])
            
    down = []
    for i in range(n-1,-1,-1):
        while len(down) > 1 and ccw(down[-2],down[-1],points[i]) <= 0:
            down.pop()
        down.append(points[i])
    
    return  up[:-1] + down[:-1]

N = int(sys.stdin.readline())
lst = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
lst = convexhull(lst)
print(isparallel(lst))


