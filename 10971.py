from itertools import permutations
import sys
input = sys.stdin.readline
## 순열 nPr

n = int(input())

cost= [list(map(int,input().split())) for _ in range(n)]
list = list(permutations(range(n)))
ans = 0
for route in list:
    print('route =', route)
    mark = True
    sum = 0
    for i in range(n-1):
        if cost[route[i]][route[i+1]] == 0:
            mark = False
            break 
        else: sum += cost[route[i]][route[i+1]]
    if cost[route[-1]][route[0]] == 0:
        mark = False
    else: sum += cost[route[-1]][route[0]]
    
    
    if mark and (ans == 0 or ans>sum) :
        ans = sum

print(ans)



1234