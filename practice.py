N = int(input())
lst = list(map(int,input().split()))
ans = 0
for i in range(len(lst)):
    for j in range(i,len(lst)):
        ans += abs(lst[i]-lst[j])
print(ans)