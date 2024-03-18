import sys
from itertools import permutations

N , M = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
ans = list(permutations(arr , M))
ans.sort()
for i in ans:
    print(*list(i))