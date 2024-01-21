import sys

def updown(a, lists, check):
    count = 1
    check[a] = True
    for i in lists[a]:
        if not check[i]:
            count += updown(i, lists, check)
    return count

N, M = map(int, sys.stdin.readline().split())

_low = [[] for _ in range(N+1)]
_high = [[] for _ in range(N+1)]
mid = (N+1)//2

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    _low[b].append(a)
    _high[a].append(b)

ans = 0

for i in range(1, N+1):
    check_low = [False] * (N+1)
    check_high = [False] * (N+1)
    
    if len(_low[i]) != 0 and not check_low[i]:
        a_count = updown(i, _low, check_low) - 1
        if a_count >= mid:
            ans += 1

    if len(_high[i]) != 0 and not check_high[i]:
        b_count = updown(i, _high, check_high) - 1
        if b_count >= mid:
            ans += 1

print(ans)
