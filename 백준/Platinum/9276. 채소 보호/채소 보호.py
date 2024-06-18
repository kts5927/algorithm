import sys

##AB 벡터
def add(A, B):
    return [A[0] + B[0], A[1] + B[1]]

##BA 벡터
def subtract(A, B):
    return [A[0] - B[0], A[1] - B[1]]

## 내적
def dot(A, B):
    return A[0] * B[0] + A[1] * B[1]

##외적
def cross(A, B):
    return A[0] * B[1] - A[1] * B[0]

##단순거리
def dist(A, B):
    dx = A[0] - B[0]
    dy = A[1] - B[1]
    return (dx * dx + dy * dy) ** 0.5

##ccw
def ccw(A, B, C):
    return A[0] * B[1] + B[0] * C[1] + C[0] * A[1] - A[1] * B[0] - B[1] * C[0] - C[1] * A[0]

def dist2(x, y, z):
    t = add(x, z)
    return abs(cross(subtract(y, x), subtract(t, x))) / dist(x, t)

def convex_hull(points):
    points.sort()
    L, R = [], []
    for p in points:
        while len(L) > 1 and ccw(L[-2], L[-1], p) <= 0:
            L.pop()
        L.append(p)
        while len(R) > 1 and ccw(R[-2], R[-1], p) >= 0:
            R.pop()
        R.append(p)
    R.reverse()
    return L[:-1] + R[:-1]

input = sys.stdin.read
data = input().strip().split('\n')
idx = 0

while idx < len(data):
    n = int(data[idx].strip())
    if n == 0:
        break
    idx += 1
    points = [list(map(int, data[idx + i].split())) for i in range(n)]
    idx += n

    points = convex_hull(points)
    n = len(points)

    if n == 1:
        print(0.0)
    elif n == 2:
        print(2.0 * dist(points[0], points[1]))
    else:
        r1, r2, r3 = 1, 1, 1
        ans = float('inf')
        for i in range(n):
            if r1 % n == i:
                r1 += 1
            if r2 % n == i:
                r2 += 1
            if r3 % n == i:
                r3 += 1
            
            while ccw(points[i], points[(i + 1) % n], add(subtract(points[(r1 + 1) % n], points[r1 % n]), points[(i + 1) % n])) > 0 and dot(subtract(points[(i + 1) % n], points[i]), subtract(points[(r1 + 1) % n], points[r1 % n])) > 0:
                r1 += 1
            while ccw(points[i], points[(i + 1) % n], add(subtract(points[(r2 + 1) % n], points[r2 % n]), points[(i + 1) % n])) > 0:
                r2 += 1
            while ccw(points[i], points[(i + 1) % n], add(subtract(points[(r3 + 1) % n], points[r3 % n]), points[(i + 1) % n])) > 0 or dot(subtract(points[(i + 1) % n], points[i]), subtract(points[(r3 + 1) % n], points[r3 % n])) < 0:
                r3 += 1
            
            p = subtract(points[(i + 1) % n], points[i])
            ans = min(ans, (dist2(points[i], points[r2 % n], p) + dist2(points[r1 % n], points[r3 % n], [p[1], -p[0]])) * 2)
        
        print(f"{ans:.6f}")
