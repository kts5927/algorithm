def decimal_to_base(n, b):
    result = ""
    while n > 0:
        remainder = n % b
        if remainder < 10:
            result += str(remainder)
        else:
            result += chr(remainder - 10 + ord('A'))
        n //= b
    return result[::-1] 

n, b = map(int, input().split())
print(decimal_to_base(n, b))
