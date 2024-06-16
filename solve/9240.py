import sys
import io


def ccw(a,b,c) :
    return (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])

def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5



T = int(input())
arrow = []
for i in range(T):
    arrow.append(list(map(int,sys.stdin.readline().split())))

arrow.sort()

cal_1 = []
for i in range(T):
    while len(cal_1) > 1:
        if ccw(cal_1[-2],cal_1[-1],arrow[i]) > 0:
            break
        cal_1.pop()
    cal_1.append(arrow[i])
    
cal_2 = []
for i in range(T-1,-1,-1):
    while len(cal_2) > 1:
        if ccw(cal_2[-2],cal_2[-1],arrow[i]) > 0:
            break
        cal_2.pop()
    cal_2.append(arrow[i])    
    

cal = cal_1[:-1] + cal_2[:-1]
size = len(cal)

ans = 0
for i in range(size):
    for j in range(i + 1, size):
        ans = max(ans, distance(cal[i], cal[j]))        
print(ans)