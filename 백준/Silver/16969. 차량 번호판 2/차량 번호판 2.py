MOD = 1_000_000_009

format_str = input().strip()

result = 26 if format_str[0] == 'c' else 10

for i in range(1, len(format_str)):
    if format_str[i] == 'c':
        if format_str[i] == format_str[i - 1]:
            result = (result * 25) % MOD
        else:
            result = (result * 26) % MOD
    else:  # format_str[i] == 'd'
        if format_str[i] == format_str[i - 1]:
            result = (result * 9) % MOD
        else:
            result = (result * 10) % MOD

print(result)
