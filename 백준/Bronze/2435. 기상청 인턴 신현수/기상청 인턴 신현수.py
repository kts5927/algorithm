N , K = map(int,input().split())
lst = list(map(int,input().split()))
L = 0
ans = -float('inf')
while L < N-K+1:
    cal = sum(lst[L:L+K])
    ans = max(ans,cal)
    L += 1
print(ans)