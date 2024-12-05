from math import comb

mod = 10**9+7

comb_arr = [comb((1 << (i + 1)) - 2, (1 << i) - 1) % mod for i in range(11)]

DP = [1]
for i in range(10):
    DP.append(DP[-1]**2 * comb_arr[i + 1] % mod)

n = int(input())
print(DP[n])
