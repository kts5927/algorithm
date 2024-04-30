N, M = map(int,input().split())
lst = [[] for _ in  range(M)]

min_bound = float('inf')
min_one = float('inf')
for i in range(M):
    A , B = map(int,input().split())
    min_bound = min(min_bound, A)

    min_one = min(min_one, B)

if min_bound < min_one * 6:
    if min_bound < (N % 6) * min_one:
        print((N // 6) * min_bound + min_bound)
    else:
        print((N // 6) * min_bound + (N % 6) * min_one)

elif min_bound >= min_one * 6:
    print(N * min_one)