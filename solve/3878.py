import sys

def ccw(a,b,c):
    return (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])

def isInside(lst,point) :
    if len(lst) <= 2:
        return True
    
    else:
        base = ccw(lst[0], lst[1], point)
        length = len(lst)
        for i in range(length) :
            cw = ccw(lst[i],lst[(i+1)%length],point)
            if cw * base <= 0: 
                return True
        return False


def check(a,b,c,d):
    if a > b:
        a,b = b,a
    if c>d:
        c,d = d,c
    
    return b<c or d<a

def cross(a,b,c,d):
    ab = ccw(a,b,c) * ccw(a,b,d)
    cd = ccw(c,d,a) * ccw(c,d,b)
    if ab==0 and cd==0:
        return not check(a[0],b[0],c[0],d[0]) and not check(a[1],b[1],c[1],d[1])
    return ab<=0 and cd<=0

def convexhull(points , color):
    points.sort()
    cal_1 = []
    cal_2 = []
    
    for i in range(color):
        while len(cal_1) > 1 and ccw(cal_1[-2] , cal_1[-1] , points[i]) <= 0:
            cal_1.pop()
        cal_1.append(points[i])

        while len(cal_2) > 1 and ccw(cal_2[-2] , cal_2[-1] , points[i]) >= 0:
            cal_2.pop()
        cal_2.append(points[i])
    
    cal_2.reverse()
    
    return cal_1[:-1] + cal_2[:-1]

T = int(sys.stdin.readline())
answer = []
for _ in range(T):
    B,W = map(int,sys.stdin.readline().split())
    
    Black = []
    White = []
    
    for b in range(B):
        x , y = map(int,sys.stdin.readline().split())
        Black.append([x,y])
        
    for w in range(W):
        x , y = map(int,sys.stdin.readline().split())
        White.append([x,y])
        
    if B > 1:
        Black = convexhull(Black, B)
    if W > 1:
        White = convexhull(White, W)

    B_len = len(Black)
    W_len = len(White)
    ans = True
    for i in range(B_len):
        if isInside(White,Black[i]) == False:
            ans = False
    for i in range(W_len):
        if isInside(Black,White[i]) == False:
            ans = False  
    
    for i in range(B_len):
        for j in range(W_len):
            if cross(Black[i],Black[(i+1)%B_len],White[j],White[(j+1)%W_len]):
                ans = False
    if ans:
        answer.append('YES')
    else:
        answer.append('NO')
    
for i in answer:
    print(i)
        