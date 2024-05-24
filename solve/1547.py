N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
ans = 1
for i in lst:
    if ans  in i:
        if ans != i[0]:
           ans = i[0]
        else:
            ans = i[1]
print(ans)