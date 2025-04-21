N,M = map(int,input().split())
ground = list(map(int,input().split()))
order = [0 for _ in range(N)]
for i in range(M):
    a,b,h = map(int,input().split())
    order[a-1] += h
    if b < N:
        order[b] -= h

work = 0
for i in range(N):
    work += order[i]
    ground[i] += work
print(*ground)

# -2 1 2 3 4 6 5 2 1 0
