import sys
input = sys.stdin.readline

def ccw(a, b):
    return a[0] * b[1] - b[0] * a[1]

def ccw_three(a, b, c):
    val = ccw((b[0] - a[0], b[1] - a[1]), (c[0] - a[0], c[1] - a[1]))
    if val > 0:
        return 1
    if val < 0:
        return -1
    return 0

def monotone_chain(points):
    points = sorted(points)
    lower = []
    for p in points:
        while len(lower) >= 2 and ccw_three(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and ccw_three(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

def area(a, b, c):
    return abs(a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - (b[0] * a[1] + c[0] * b[1] + a[0] * c[1]))

def solve():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]

    hull = monotone_chain(points)

    if len(hull) == 3:
        val = area(hull[0], hull[1], hull[2])
        print(f"{val // 2}{'.5' if val % 2 else ''}")
        return

    n = len(hull)
    ans = 0

    for i in range(n):
        p = (i + 1) % n
        q = (i + 3) % n

        for j in range(i + 2, n):
            if i == 0 and j == n - 1:
                continue

            while area(hull[i], hull[j], hull[p]) <= area(hull[i], hull[j], hull[(p + 1) % n]):
                p = (p + 1) % n

            while area(hull[i], hull[j], hull[q]) <= area(hull[i], hull[j], hull[(q + 1) % n]):
                q = (q + 1) % n

            now = area(hull[i], hull[j], hull[p]) + area(hull[i], hull[j], hull[q])
            ans = max(ans, now)

    print(f"{ans // 2}{'.5' if ans % 2 else ''}")

t = int(input())
for _ in range(t):
    solve()

