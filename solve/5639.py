import sys
sys.setrecursionlimit(10**9)
arr = []

while True:
    try:
        a = int(input())
        arr.append(a)
    except:
        break
def sol(a:list):
    if len(a) == 0:
        return
    left,right = [],[]
    mid = a[0]
    
    for i in range(1,len(a)):
        if a[i]>mid:
            left = a[1:i]
            right = a[i:]
            break
    else : 
        left = a[1:]
    sol(left)
    sol(right)
    print(mid)
    
sol(arr)