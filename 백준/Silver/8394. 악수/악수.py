from sys import stdin

n = int(stdin.readline())

arr = [0 for _ in range(n + 1)]
arr[0] = 1
arr[1] = 1
for i in range(2, n + 1):
    arr[i] = (arr[i-1] + arr[i - 2]) % 10
print(arr[n])