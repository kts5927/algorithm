def rightmost_nonzero_digit(t, cases):
    results = []
    for n in cases:
        res = 1
        for i in range(1, n + 1):
            res *= i
            
            while res % 10 == 0:
                res //= 10
            
            res %= 100000
        
        results.append(res % 10)
    
    return results

t = int(input())
cases = [int(input()) for _ in range(t)]

for result in rightmost_nonzero_digit(t, cases):
    print(result)
