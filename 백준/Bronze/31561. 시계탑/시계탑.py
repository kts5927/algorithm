M = int(input())

if M <= 30:
    result = M / 2
else:
    result = 15 + (M - 30) * (3 / 2)


print(f"{result:.1f}")