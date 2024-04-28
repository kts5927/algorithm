N = int(input())
ans = 0
i = 1
while i < N:
    cal = (N - 1) // ((N - 1) // i)
    ans += ((N - 1) // i) * (cal - i + 1)
    i = cal+1
print(ans + N)
