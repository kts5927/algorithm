import sys
input = sys.stdin.readline

def cal(a,b,t):
    cal = (a+t)%(2*b)
    if cal > b:
        cal = 2*b - cal
    return cal

def sol():
    w,h = map(int,input().split())
    p,q = map(int,input().split())
    t = int(input())

    print(cal(p,w,t),cal(q,h,t))
sol()