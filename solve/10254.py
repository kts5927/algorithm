import sys

def ccw(a,b,c):
    return (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])

def cccw(a,b,c,d):
    tmp = d[:]
    tmp[0] -= (c[0] - b[0])
    tmp[1] -= (c[1] - b[1])
    return ccw(a,b,tmp)

def distance(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2


T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    city = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    city.sort()
    
    
    cal_1 = []
    for i in range(N):
        while len(cal_1) > 1 and ccw(cal_1[-2],cal_1[-1],city[i]) <= 0:
            cal_1.pop()
        cal_1.append(city[i])
            
    cal_2 = []
    for i in range(N-1,-1,-1):
        while len(cal_2) > 1 and ccw(cal_2[-2],cal_2[-1],city[i]) <= 0:
            cal_2.pop()
        cal_2.append(city[i])
    
    cal = cal_1[:-1] + cal_2[:-1]
    num = len(cal)

    MAX = 0
    j = 1
    ans = [[],[]]
    for i in range(num):
        while j+1 != i and cccw(cal[i],cal[(i+1)%num],cal[j%num],cal[(j+1)%num]) > 0:
            if distance(cal[i],cal[j%num]) > MAX:
                ans[0] = cal[i]
                ans[1] = cal[j%N]
                MAX = distance(cal[i],cal[j%num])
            j += 1
        if distance(cal[i],cal[j%num]) > MAX:
                ans[0] = cal[i]
                ans[1] = cal[j%num]
                MAX = distance(cal[i],cal[j%num])
                
    print(*ans[0],*ans[1])