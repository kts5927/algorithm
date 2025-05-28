import math

N, D, p = map(int, input().split())
A = list(map(int, input().split()))

turns = 0

while True:
    target = -1
    for i in range(N):
        if A[i] > 0:
            target = i
            break

    if target == -1:
        break 

    A[target] -= D
    turns += 1

    if A[target] < 0 and target + 1 < N and A[target + 1] > 0:
        overkill = -A[target]
        splash = math.floor(overkill * p / 100)
        A[target + 1] -= splash

print(turns)
