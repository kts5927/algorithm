import sys
from bisect import bisect_left
input = sys.stdin.readline

N, M = map(int, input().split())

State = []
limits = []

for i in range(N):
    name, value = input().split()
    State.append((name, int(value)))
    limits.append(int(value))

for _ in range(M):
    CP = int(input())
    idx = bisect_left(limits, CP)
    print(State[idx][0])