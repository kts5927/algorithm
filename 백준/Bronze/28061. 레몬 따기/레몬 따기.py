N = int(input())
a = list(map(int, input().split()))

max_lemons = 0
for i in range(N):
    lemons_collected = a[i]
    steps = (N + 1) - (i + 1)  # 이동 횟수
    lemons_taken_home = lemons_collected - steps
    if lemons_taken_home > max_lemons:
        max_lemons = lemons_taken_home

print(max_lemons)
