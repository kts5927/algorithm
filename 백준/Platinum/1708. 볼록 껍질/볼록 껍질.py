import sys

def ccw (a,b,c):
    return (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])


N = int(sys.stdin.readline())
points = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
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
points = L[:-1] + R[:-1]
n = len(points)

print(n)