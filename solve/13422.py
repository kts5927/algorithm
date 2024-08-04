import sys

T = int(sys.stdin.readline())

for i in range(T):
    N , M , K = map(int,sys.stdin.readline().split())
    lst = list(map(int,sys.stdin.readline().split()))
    
    
    if N == M:
        print(sum(lst))
        if K > sum(lst):
            print(1)
        else:
            print(0)
    else:
        lst = lst+lst
        l = 0
        r = M-1
        cal = 0
        ans = 0
        for i in range(r+1):
            cal += lst[i]
        while l < N:
            cal -= lst[l]
            l += 1
            r += 1
            cal += lst[r]
            if cal < K:
                ans += 1
                
        print(ans)
