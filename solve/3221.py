import sys
input = sys.stdin.readline

L, T = map(int, input().split())
N = int(input())
ants = []

for i in range(N):
    pos, direction = input().split()
    pos = int(pos)
    if direction == 'D':
        ants.append((pos + T, i))  
    else:
        ants.append((pos - T, i)) 

final_positions = [(pos % (2 * L)) for pos, i in ants]

for i in range(len(final_positions)):
    if final_positions[i] > L:
        final_positions[i] = 2 * L - final_positions[i]

final_positions = sorted((final_positions[i], ants[i][1]) for i in range(N))

print(' '.join(str(pos) for pos, _ in final_positions))
