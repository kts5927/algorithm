N = int(input())
lst = list(map(int, input().strip()))

ans = 0
cal = 0

for i in lst:
    if i == 0:
        if cal * 10 + i > 641:
            ans += 2
            cal = i
        else:
            cal = cal * 10
    else:
        if cal * 10 + i > 641:
            ans += 1
            cal = i
        else:
            cal = cal * 10 + i

if cal != 0:
    ans += 1

print(ans)
