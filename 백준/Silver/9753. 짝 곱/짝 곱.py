import math

def prime(limit):
    lst = [True] * (limit + 1)
    lst[0], lst[1] = False, False
    
    for i in range(2, int(limit**0.5 + 1)):
        if lst[i]:
            for j in range(i * i, limit + 1, i):
                lst[j] = False
                
    primes = [i for i, prime in enumerate(lst) if prime]
    return primes

def cal(K, primes):
    product = float('inf')
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            Cal = primes[i] * primes[j]
            if Cal >= K:
                product = min(product,Cal)
                break
    return product


T = int(input())  
cases = [int(input()) for _ in range(T)]

primes = prime(100001)

for K in cases:
    result = cal(K, primes)
    print(result)
