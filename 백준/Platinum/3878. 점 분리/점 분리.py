import sys
import math

input = sys.stdin.readline

def cross(x1, y1, x2, y2, x3, y3, x4, y4):
    if x1 == x2:
        x = x1
        y = (y4 - y3) * (x - x3) / (x4 - x3) + y3
    elif x3 == x4:
        x = x3
        y = (y2 - y1) * (x - x1) / (x2 - x1) + y1
    else:
        x = ((y4 - y3) * x3 / (x4 - x3) - (y2 - y1) * x1 / (x2 - x1) + y1 - y3) / ((y4 - y3) / (x4 - x3) - (y2 - y1) / (x2 - x1))
        y = (y2 - y1) * (x - x1) / (x2 - x1) + y1
    return x, y

def check(x, y, x1, y1, x2, y2, x3, y3, x4, y4):
    if not min(x1, x2) - 0.0000001 <= x <= max(x1, x2) + 0.0000001:
        return 0
    if not min(x3, x4) - 0.0000001 <= x <= max(x3, x4) + 0.0000001:
        return 0
    if not min(y1, y2) - 0.0000001 <= y <= max(y1, y2) + 0.0000001:
        return 0
    if not min(y3, y4) - 0.0000001 <= y <= max(y3, y4) + 0.0000001:
        return 0
    return 1

def lineCross(x1, y1, x2, y2, x3, y3, x4, y4):
    if x1 == x2 and x3 == x4:
        if x1 == x3:
            if max(y1, y2) < min(y3, y4):
                return 0
            elif max(y3, y4) < min(y1, y2):
                return 0
            else:
                return 1
        else:
            return 0
    elif (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1):
        if (y3 - y1) * (x2 - x1) == (y2 - y1) * (x3 - x1):
            if max(x1, x2) < min(x3, x4):
                return 0
            elif max(x3, x4) < min(x1, x2):
                return 0
            else:
                return 1
        else:
            return 0
    else:
        x, y = cross(x1, y1, x2, y2, x3, y3, x4, y4)
        return check(x, y, x1, y1, x2, y2, x3, y3, x4, y4)

def ccw(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]

def ccwP(p1, p2, p3):
    v1 = [p2[0] - p1[0], p2[1] - p1[1]]
    v2 = [p3[0] - p1[0], p3[1] - p1[1]]
    return ccw(v1, v2)

def convexHull(points):
    points.sort(key=lambda x: (x[1], x[0]))
    x0, y0 = points[0]
    slope = []
    for i in range(1, len(points)):
        x, y = points[i]
        if x == x0:
            slope.append([i, 90])
        else:
            temp = math.degrees(math.atan((y - y0) / (x - x0)))
            if temp < 0:
                temp = 180 + temp
            slope.append([i, temp])
    slope.sort(key=lambda x: x[1])
    slope.append([0, 0])
    stack = []
    stack.append([x0, y0])
    stack.append(points[slope[0][0]])
    for i, dummy in slope:
        x, y = points[i]
        p1 = stack[-2]
        p2 = stack[-1]
        v1 = p2[0] - p1[0], p2[1] - p1[1]
        v2 = x - p1[0], y - p1[1]
        c = ccw(v1, v2)
        while c <= 0:
            stack.pop()
            if len(stack) == 1:
                break
            p1 = stack[-2]
            p2 = stack[-1]
            v1 = p2[0] - p1[0], p2[1] - p1[1]
            v2 = x - p1[0], y - p1[1]
            c = ccw(v1, v2)
        stack.append([x, y])
    stack.pop()
    return stack

def inside(ch, p):
    l = len(ch)
    for i in range(l):
        p1, p2 = ch[i], ch[(i + 1) % l]
        if ccwP(p1, p2, p) < 0:
            return False
    return True

t = int(input())
for tt in range(t):
    n, m = map(int, input().split())
    black = []
    white = []
    for i in range(n):
        black.append(list(map(int, input().split())))
    for i in range(m):
        white.append(list(map(int, input().split())))

    ch1 = convexHull(black)
    ch2 = convexHull(white)

    if len(ch1) == 1 and len(black) != 1:
        ch1.append(black[-1])

    if len(ch2) == 1 and len(white) != 1:
        ch2.append(white[-1])

    l1 = len(ch1)
    l2 = len(ch2)

    if l1 == 1 and l2 == 1:
        print("YES")
        continue

    if l1 == 1 and l2 == 2:
        p = ch1[0]
        p1 = ch2[0]
        p2 = ch2[1]
        if ccwP(p1, p2, p) == 0:
            if p1[0] < p[0] < p2[0]:
                print("NO")
                continue
        print("YES")
        continue

    if l2 == 1 and l1 == 2:
        p = ch2[0]
        p1 = ch1[0]
        p2 = ch1[1]
        if ccwP(p1, p2, p) == 0:
            if p1[0] < p[0] < p2[0]:
                print("NO")
                continue
        print("YES")
        continue

    if l1 == 2 and l2 == 2:
        x1, y1 = ch1[0]
        x2, y2 = ch1[1]
        x3, y3 = ch2[0]
        x4, y4 = ch2[1]
        if lineCross(x1, y1, x2, y2, x3, y3, x4, y4) == 1:
            print("NO")
        else:
            print("YES")
        continue

    if l1 == 1 and l2 > 2:
        if inside(ch2, ch1[0]):
            print("NO")
        else:
            print("YES")
        continue

    if l2 == 1 and l1 > 2:
        if inside(ch1, ch2[0]):
            print("NO")
        else:
            print("YES")
        continue

    answer = "YES"
    for i in range(l1):
        x1, y1 = ch1[i]
        x2, y2 = ch1[(i + 1) % l1]
        for j in range(l2):
            x3, y3 = ch2[j]
            x4, y4 = ch2[(j + 1) % l2]
            if lineCross(x1, y1, x2, y2, x3, y3, x4, y4) == 1:
                answer = "NO"
                break
        if answer == "NO":
            break

    if answer == "YES":
        if l1 > 2 and l2 > 2:
            if inside(ch2, ch1[0]) or inside(ch1, ch2[0]):
                answer = "NO"
        elif l1 == 2:
            if inside(ch2, ch1[0]):
                answer = "NO"
        else:
            if inside(ch1, ch2[0]):
                answer = "NO"

    print(answer)
