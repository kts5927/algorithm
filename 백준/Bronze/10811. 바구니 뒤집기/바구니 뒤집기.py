N, M = map(int, input().split())
lst = [i for i in range(1, N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    lst[a-1:b] = reversed(lst[a-1:b])

print(*lst)
