from itertools import permutations

N , M = map(int,input().split())
lst = list(map(int,input().split()))
ans = list(set(permutations(lst , M)))
ans.sort()
for i in ans:  
    print(*i)