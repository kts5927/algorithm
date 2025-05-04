N = int(input())
ans = 0
for i in range(N):
    ans += sum(list(map(int,input().split())))
print(ans)