import sys
import math

def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

T = int(input())
arrow = []

for i in range(T):
    arrow.append(list(map(int, input().split())))

# x, y 좌표 기준으로 정렬
arrow.sort()

# Convex Hull 계산
cal_1 = []
for i in range(T):
    while len(cal_1) > 1 and ccw(cal_1[-2], cal_1[-1], arrow[i]) <= 0:
        cal_1.pop()
    cal_1.append(arrow[i])

cal_2 = []
for i in range(T - 1, -1, -1):
    while len(cal_2) > 1 and ccw(cal_2[-2], cal_2[-1], arrow[i]) <= 0:
        cal_2.pop()
    cal_2.append(arrow[i])

cal = cal_1[:-1] + cal_2[:-1]
size = len(cal)

# 가장 먼 두 점 사이의 거리 계산
ans = 0
for i in range(size):
    for j in range(i + 1, size):
        ans = max(ans, distance(cal[i], cal[j]))

print(ans)
