N = int(input())
P = list(map(int, input().split()))

freeze_available = True
can_attach_day = -1
current_streak = 0
max_streak = 0

for i in range(N):
    if can_attach_day == i:
        freeze_available = True

    if P[i] > 0:
        current_streak += 1
    else:
        if freeze_available:
            freeze_available = False
            can_attach_day = i + 2
        else:
            current_streak = 0  

    max_streak = max(max_streak, current_streak)

print(max_streak)
