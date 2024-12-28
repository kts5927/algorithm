import sys
input = sys.stdin.readline

def PrintHive(Hive, depth):
    for room, subrooms in sorted(Hive.items()):
        print("--" * depth + room)
        PrintHive(subrooms, depth + 1)

N = int(input())

Hive = {}
for i in range(N):
    room = list(map(str, input().split()))
    now = Hive
    for i in range(1, int(room[0]) + 1):
        if room[i] not in now:
            now[room[i]] = {}
        now = now[room[i]]

PrintHive(Hive, 0)
