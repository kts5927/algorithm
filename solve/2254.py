import sys

def ccw(a,b,c):
    return (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])

def convexhull(points):
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

def is_inside(cal):
    n = len(cal)
    for i in range(n):
        if ccw(cal[i],cal[(i+1)%n],[Px,Py]) < 0:
            return False
    return True


T , Px , Py = map(int,sys.stdin.readline().split())

points = [list(map(int,sys.stdin.readline().split())) for _ in range(T)]

points.sort()
ans = 0
while True:
    cal = convexhull(points)
    if is_inside(cal):
        ans += 1
        for i in cal:
            points.remove(i)
    else:
        break
    if len(points) < 3:
        break
print(ans)

