import math

def factorize_quadratic(n):
    a = n
    b = n + 1
    c = -(n + 2)

    d = b**2 - 4 * a * c

    if d < 0:
        return -1

    sd = math.isqrt(d)
    if sd * sd != d:
        return -1

    x1 = (-b + sd) / (2 * a)
    x2 = (-b - sd) / (2 * a)

    if x1.is_integer() and x2.is_integer():
        x1, x2 = int(x1), int(x2)
        return (a, -x1 * a, 1, -x2)
    else:
        return -1

n = int(input())
result = factorize_quadratic(n)

if result == -1:
    print(-1)
else:
    print(*result)
