import sys

def ccw (a,b,c) :
    return ( a[0] * b[1] + b[0] * c[1] + c[0] * a[1] ) - ( a[1] * b[0] + b[1] * c[0] + c[1] * a[0] )

T = int(sys.stdin.readline())
points = [list(map(int,sys.stdin.readline().split())) for _ in range(T)]

start , end = map(int,sys.stdin.readline().split())

if (start - end) % T in [1, T - 1]:
    print(2)
    print(start, end)
    exit()

check = False
if start == 0 or (end != 0 and start > end):
    start,end = end,start
    check = True

cal = [start,(start+1)%T]

for i in range(start+2,start+T):
    i = i%T

    while len(cal) >=2 and  ccw(points[cal[-2]],points[cal[-1]],points[i]) >= 0:
        cal.pop()
    cal.append(i)
    if i == end:
        break
if check:
    cal.reverse()
print(len(cal))
print(*cal)