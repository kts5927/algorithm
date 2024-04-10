import sys
N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))

a = max(lst)
cost = [0 for _ in range(a+1)]

for i in lst:
    cost[i] += 1

ans = 0
for i in range(a,0,-1):
    while cost[i] != 0:
        count = 0
        while cost[i-count] != 0 :
            cost[i-count] -= 1
            ans += i
            count += 1


print(ans)