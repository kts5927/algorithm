from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
permutations_list = list(permutations(range(n)))
ans = float('inf')

for perm in permutations_list:
    mark = True
    cur_sum = 0
    
    for i in range(n-1):
        if cost[perm[i]][perm[i+1]] == 0:
            mark = False
            break 
        else:
            cur_sum += cost[perm[i]][perm[i+1]]

    if cost[perm[-1]][perm[0]] == 0:
        mark = False
    else:
        cur_sum += cost[perm[-1]][perm[0]]
    
    if mark and cur_sum < ans:
        ans = cur_sum

print(ans)