from itertools import permutations

N = int(input())
ans = list(permutations(range(1,N+1),N))
for i in ans:
    print(*i,end='\n')
