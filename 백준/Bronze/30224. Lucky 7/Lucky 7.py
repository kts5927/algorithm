N = int(input())
ans = 0
if N%7 == 0:
    ans += 1
N = str(N)
N = list(map(str,N))
for i in N:
    if i == '7':
        ans += 2
        break
print(ans)