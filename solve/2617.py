import sys
N , M = map(int,sys.stdin.readline().split())
def updown(a,lists:list,check):
    count = 1
    check[a] = True
    for i in lists[a]:
        if not check[i]:
            count += updown(i,lists,check)
    return count

_low = [[] for _ in range(N+1)]
_high = [[] for _ in range(N+1)]
mid = (N+1)//2 

for i in range(M):
    a , b = map(int,sys.stdin.readline().split())
    _low[b].append(a)
    _high[a].append(b)
ans = 0
for i in range(1,N+1):

    check_low = [False for _ in range(N+1)]
    if len(_low[i]) != 0:
        a = updown(i,_low,check_low) - 1
        if a >= mid :
            ans += 1
    check_high = [False for _ in range(N+1)]
    if len(_high[i]) != 0:
        b = updown(i,_high,check_high) - 1
        if b >=mid: 
            ans += 1
    
print(ans)

