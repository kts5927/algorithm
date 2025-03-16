T = int(input())
for i in range(T):
    N,D = map(int,input().split())
    ans = 0
    for j in range(N):
        v,f,c = map(int,input().split())
        a = v*f//c
        if v*f//c >= D:
            ans += 1
    print(ans)