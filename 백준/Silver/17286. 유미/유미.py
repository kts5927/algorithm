import itertools
import math

yumi_x, yumi_y = map(int, input().strip().split())
people = [tuple(map(int, input().strip().split())) for _ in range(3)]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

min_distance = float('inf')

for perm in itertools.permutations(people):
    current_distance = 0
    current_position = (yumi_x, yumi_y)

    for person in perm:
        current_distance += euclidean_distance(current_position, person)
        current_position = person
    
    min_distance = min(min_distance, current_distance)

print(int(min_distance))
