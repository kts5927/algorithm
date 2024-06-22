import sys

def ccw (a,b,c) :
    return ( a[0] * b[1] + b[0] * c[1] + c[0] * a[1] ) - ( a[1] * b[0] + b[1] * c[0] + c[1] * a[0] )

T = int(sys.stdin.readline())
points = [list(map(int,sys.stdin.readline().split())) for _ in range(T)]

start , end = map(int,sys.stdin.readline().split())

cal = []
check = False
if start == 0 or (end != 0 and start > end):
    start,end = end,start
    check = True

for i in range(start,start+T):
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



# 모양 확인 도구. 예제를 오른쪽으로 90도 회전했음.
# lst = [['.' for _ in range(20)]for q in range(20)]

# for i in points:
#     lst[i[0]][i[1]] = 0

# for i in lst:
#     print(*i)
    
