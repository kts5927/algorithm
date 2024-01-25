import sys

n = int(sys.stdin.readline())

for i in range(n):
    a = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    price = int(sys.stdin.readline())
    
    costs = [0 for _ in range(price+1)]
    costs[0] = 1
    
    for coin in coins:
        for j in range(coin, price + 1):
            costs[j] += costs[j - coin]

    print(costs[-1])