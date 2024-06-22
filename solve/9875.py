import sys

def ccw(a,b,c):
    return (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])

def convexhull(list):
    
    A = []
    B = []
    
    for i in list:
        while len(A) > 1 and ccw(A[-2],A[-1],i) <= 0:
            A.pop()
        A.append(i)
    
        while len(B) > 1 and ccw(B[-2],B[-1],i) >= 0:
            B.pop()
        B.append(i)
        
    B.reverse()
    return A[:-1] + B[:-1]

def isIner(list, point):
    
    n = len(list)
    if n  == 2:
        return not ccw(list[0], list[1], point) and min(list[0], list[1]) <= point <= max(list[0], list[1])
    
    left = 0
    right = n-1
    
    while left < right:
        mid = (left + right) //2
        if ccw(list[0] , list[mid] , point)<0:
            right = mid
        else:
            left = mid+1
            
    return ccw(list[0], list[left - 1], point) >= 0 and ccw(list[left - 1], list[left], point) >= 0 and ccw(list[left], list[0], point) >= 0


T = int(sys.stdin.readline())

Ateam = sorted(list(map(int, input().split())) for _ in range(T))
Bteam = sorted(list(map(int, input().split())) for _ in range(T))

Ateam_ = convexhull(Ateam)
Bteam_ = convexhull(Bteam)


A_iner = 0
B_iner = 0

for i in range(T):
    if isIner(Ateam_,Bteam[i]):
        A_iner += 1

for i in range(T):
    if isIner(Bteam_,Ateam[i]):
        B_iner += 1


print(A_iner , B_iner)