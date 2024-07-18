import sys
arr = [0] * 10001
arr[0] = 1
N, x = map(int, sys.stdin.readline().split())
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    for i in range(x, 0, -1):
        p = 0
        for j in range(b):
            p += a
            if i - p < 0:
                break
            arr[i] += arr[i - p]
print(arr[x])

