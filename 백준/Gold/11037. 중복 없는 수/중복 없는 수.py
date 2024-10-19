from itertools import combinations, permutations
import bisect
import sys

numbers = []
digits = '123456789'

for k in range(1, 10):
    for combo in combinations(digits, k):
        for perm in permutations(combo):
            num = int(''.join(perm))
            numbers.append(num)

numbers.sort()

for line in sys.stdin:
    N = int(line.strip())
    idx = bisect.bisect_right(numbers, N)
    if idx < len(numbers):
        print(numbers[idx])
    else:
        print(0)
