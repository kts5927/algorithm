import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
cal = [0] * N 

ans = 0

for i in range(N):
    if cal[i] != lst[i]:
        ans += 1  
        cal[i] = 1 - cal[i]
        if i + 1 < N:
            cal[i + 1] = 1 - cal[i + 1]
        if i + 2 < N:
            cal[i + 2] = 1 - cal[i + 2]

print(ans)
