import sys
import math
MAX = float('inf')

def ccw(a, b, c):
    return (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])

def polar_angle(p0, p1):
    return math.atan2(p1[1] - p0[1], p1[0] - p0[0])

def distance_squared(p0, p1):
    return (p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2

def convex_hull(points):
    stk = points[:2]
    for point in points[2:]:
        while len(stk) > 1 and ccw(stk[-2], stk[-1], point) <= 0:
            stk.pop()
        stk.append(point)
    return stk

def distance(target, p0, p1):
    if p0[0] == p1[0]:
        return abs(target[0] - p0[0])
    if p0[1] == p1[1]:
        return abs(target[1] - p0[1])
    a, b = (p1[1] - p0[1]) / (p1[0] - p0[0]), -1
    c = -a * p0[0] + p0[1]
    return abs(a*target[0] + b*target[1] + c) / (a**2 + b**2) ** 0.5

def solve(idx):
    N = int(sys.stdin.readline())
    if N == 0:
        return False
    points = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    ref, *points = sorted(points)
    points.sort(key=lambda p: (polar_angle(ref, p), distance_squared(ref, p)))

    result = convex_hull([ref] + points)
    length = len(result)

    ans = MAX
    for i in range(length):
        k = (i + 1) % length
        tmp = 0.
        for j in range(length):
            tmp = max(tmp, distance(result[j], result[i], result[k]))
        ans = min(ans, tmp)

    print(f'Case {idx}: {math.ceil(ans * 100) / 100.0:.2f}')
    return True

idx = 1
while True:
    if not solve(idx):
        break
    idx += 1
