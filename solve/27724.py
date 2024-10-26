import math
n, m, k = map(int, input().split())
Max = int(math.log(n, 2))
cal = int(math.log(k, 2))
print(min(cal + m, Max))