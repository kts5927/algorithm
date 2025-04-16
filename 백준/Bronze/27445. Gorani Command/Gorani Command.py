N, M = map(int, input().split())

distances = []
for _ in range(N - 1):
    distances.append(int(input()))
distances += list(map(int, input().split()))  # (N,1) ~ (N,M)

for r in range(1, N + 1):
    for c in range(1, M + 1):
        valid = True
        for i in range(N - 1):
            if abs(r - (i + 1)) + abs(c - 1) != distances[i]:
                valid = False
                break
        if not valid:
            continue
        for j in range(M):
            if abs(r - N) + abs(c - (j + 1)) != distances[N - 1 + j]:
                valid = False
                break
        if valid:
            print(r, c)
            exit()
