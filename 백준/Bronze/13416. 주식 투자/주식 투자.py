def max_profit(test_cases):
    results = []
    for profits in test_cases:
        total_profit = 0
        for profit in profits:
            max_daily_profit = max(profit)  
            if max_daily_profit > 0:
                total_profit += max_daily_profit 
        results.append(total_profit)
    return results

import sys

input = sys.stdin.read
data = input().strip().split('\n')

T = int(data[0]) 
index = 1
test_cases = []

for _ in range(T):
    N = int(data[index])
    index += 1
    profits = []
    for _ in range(N):
        profits.append(list(map(int, data[index].split())))
        index += 1
    test_cases.append(profits)

results = max_profit(test_cases)

for result in results:
    print(result)
