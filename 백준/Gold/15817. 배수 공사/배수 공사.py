import sys

arr = [0] * 10001
arr[0] = 1

N, x = map(int, sys.stdin.readline().split())

for _ in range(N):
    L, C = map(int, sys.stdin.readline().split())
    for i in range(x, 0, -1):
        LL = 0
        for j in range(C):
            LL += L
            if i - LL < 0:
                break
            arr[i] += arr[i - LL]

print(arr[x])

