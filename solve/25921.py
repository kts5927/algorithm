def cal(n):
    c = [0] * (n + 1)
    ans = 0
    for i in range(2, n + 1):
        if c[i] != 0:
            continue
        c[i] = i
        ans += i
        for j in range(i, n + 1, i):
            if c[j] != 0:
                continue
            c[j] = i
            ans += i
    return ans
n = int(input())
print(cal(n))
