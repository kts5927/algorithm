lst = list(map(str,input().strip()))
len_lst = len(lst)
ans = 0
for i in range(len_lst):
    if lst[i] == 'Y':
        N = i
        while N < len_lst :
            lst[N] = 'N' if lst[N] == 'Y' else 'Y'
            N += i+1
        ans += 1
print(ans)