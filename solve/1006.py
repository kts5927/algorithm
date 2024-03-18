import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N , W = map(int,sys.stdin.readline().split())
    ans = N*2
    arr1 = list(map(int,sys.stdin.readline().split()))
    arr2 = list(map(int,sys.stdin.readline().split()))
    
    shadow1 = [False for i in range(N)]
    shadow2 = [False for i in range(N)]
    
    for k in range(N):
        if not shadow1[k] and not shadow1[k-1] and W >= arr1[k] + arr1[k-1]:
            shadow1[k-1] = True
            shadow1[k] = True
            ans -= 1
        if not shadow2[k] and not shadow2[k-1] and W >= arr2[k] + arr2[k-1]:
            shadow2[k-1] = True
            shadow2[k] = True
            ans -= 1
        if not shadow1[k] and not shadow2[k] and W >= arr1[k] + arr2[k]:
            shadow1[k] = True
            shadow2[k] = True
            ans -= 1
    print('ans = ',ans)
    print(shadow1)
    print(shadow2)       

# 6 10
# 9 2 2 7 5 4
# 4 2 10 1 2 7
# ans  = 7

# 5 6
# 3 1 2 4 2
# 5 6 1 3 2
# ans = 6