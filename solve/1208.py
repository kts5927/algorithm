from itertools import combinations
from math import floor, ceil
import sys
from bisect import bisect_right

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr1 = arr[:ceil(N / 2)]
arr2 = arr[ceil(N / 2):]

sub1 = []
sub2 = []

for number in range(len(arr1) + 1):
    for sub in combinations(arr1, number):
        sub1.append(sum(sub))

for number in range(len(arr2) + 1):
    for sub in combinations(arr2, number):
        sub2.append(sum(sub))

sub1.sort()

ans = 0
for i in sub2:
    sum_ = S - i
    count = bisect_right(sub1, sum_) - bisect_right(sub1, sum_ - 1)
    ans += count

if S == 0:
    ans -= 1

print(ans)