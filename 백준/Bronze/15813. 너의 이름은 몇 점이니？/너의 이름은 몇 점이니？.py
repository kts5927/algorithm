N = int(input())
string = list(map(str,input().strip()))
ans = 0
for i in range(N):
    ans += ord(string[i])
    ans -= 64
print(ans)