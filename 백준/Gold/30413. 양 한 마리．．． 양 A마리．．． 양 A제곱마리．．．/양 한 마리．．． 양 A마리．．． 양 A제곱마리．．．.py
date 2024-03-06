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

# 등비수열의 합 공식을 사용하여 계산
# 등비수열의 합: a * (1 - r^n) / (1 - r)
# 여기서 a는 첫 번째 항, r은 등비, n은 항의 개수
# 이 문제에서는 a=1, r=A, n=B이므로,
# 합은 (1 - A^B) / (1 - A)가 됨
if A == 1:
    print(B % mod)
else:
    result = (power_mod(A, B, mod) - 1) * power_mod(A - 1, mod - 2, mod)
    print(result % mod)
