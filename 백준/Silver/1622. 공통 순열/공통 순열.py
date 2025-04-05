import sys
from collections import Counter

lines = sys.stdin.read().splitlines()
for i in range(0, len(lines), 2):
    a = lines[i]
    b = lines[i+1]

    count_a = Counter(a)
    count_b = Counter(b)

    result = []

    for ch in 'abcdefghijklmnopqrstuvwxyz':
        common = min(count_a[ch], count_b[ch])
        result.extend([ch] * common)

    print(''.join(result))
