N, M, K = map(int, input().split())
x_min = max(0, N - M * K)
x_max = max(0, N - M * (K - 1) - 1)
print(x_min, x_max)
