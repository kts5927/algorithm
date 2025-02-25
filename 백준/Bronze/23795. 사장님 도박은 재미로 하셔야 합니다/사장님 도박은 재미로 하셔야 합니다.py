import sys
input = sys.stdin.readline
ans = 0
while True:
    N = int(input())
    if N == -1:
        break
    ans += N
print(ans)