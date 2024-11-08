def factorize_quadratic(n):
    a = n
    b = n + 1
    c = -(n + 2)

    factors_a = [(i, a // i) for i in range(1, abs(a) + 1) if a % i == 0]
    factors_c = [(i, c // i) for i in range(1, abs(c) + 1) if c % i == 0]

    for (p, q) in factors_a:
        for (r, s) in factors_c:
            if p * s + q * r == b:
                return p, r, q, s
            elif p * r + q * s == b:
                return p, s, q, r

    return -1

n = int(input())
result = factorize_quadratic(n)

if result == -1:
    print(-1)
else:
    print(*result)
