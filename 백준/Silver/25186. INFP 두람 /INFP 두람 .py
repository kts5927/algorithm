n = int(input())
lst = list(map(int,input().split()))
cal = int(sum(lst))/2
ans = 'Happy'
for i in range(len(lst)):
    if cal < lst[i]:
        if n == 1:
            if lst[i] == 1:
                continue
            else:
                ans = 'Unhappy'
                break
        else:
            ans = 'Unhappy'
print(ans)
                