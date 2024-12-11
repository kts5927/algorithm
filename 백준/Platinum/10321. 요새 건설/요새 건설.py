from math import atan2

def ccw(a, b):
    return a[0] * b[1] - b[0] * a[1]

def ccw_three(a, b, c):
    val = ccw((b[0] - a[0], b[1] - a[1]), (c[0] - a[0], c[1] - a[1]))
    if val > 0:
        return 1
    if val < 0:
        return -1
    return 0

def sort_points(points):
    base = points[0]
    return sorted(points[1:], key=lambda p: (atan2(p[1] - base[1], p[0] - base[0]), p[0], p[1]))

def graham(points):
    hull = []
    for p in points:
        while len(hull) >= 2 and ccw_three(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)
    return hull

def area(a, b, c):
    return abs(a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - (b[0] * a[1] + c[0] * b[1] + a[0] * c[1]))

def solve():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]

    idx = 0
    for i in range(n):
        if points[i][0] < points[idx][0] or (points[i][0] == points[idx][0] and points[i][1] < points[idx][1]):
            idx = i

    points[0], points[idx] = points[idx], points[0]
    sorted_points = [points[0]] + sort_points(points)
    hull = graham(sorted_points)

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

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()