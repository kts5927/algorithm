# a(r^n - 1) / r - 1
#7 = 111

A, B = map(int, input().split())
mod = 1000000007

def power_mod(base, exponent, modulus):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result

if A == 1:
    print(B % mod)
else:
    result = (power_mod(A, B, mod) - 1) * power_mod(A - 1, mod - 2, mod)
    print(result % mod)
