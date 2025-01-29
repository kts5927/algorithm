import sys
from collections import defaultdict

def find_largest_artifact():
    R, C = map(int, sys.stdin.readline().split())
    N = int(sys.stdin.readline().strip())

    artifacts = defaultdict(lambda: [float('inf'), float('-inf'), float('inf'), float('-inf')])

    for _ in range(N):
        a, v, h = map(int, sys.stdin.readline().split())
        min_x, max_x, min_y, max_y = artifacts[a]
        artifacts[a] = [
            min(min_x, v),
            max(max_x, v), 
            min(min_y, h), 
            max(max_y, h)   
        ]

    max_area = -1
    best_artifact = float('inf')

    for artifact_id in sorted(artifacts.keys()):
        min_x, max_x, min_y, max_y = artifacts[artifact_id]
        area = (max_x - min_x + 1) * (max_y - min_y + 1)

        if area > max_area or (area == max_area and artifact_id < best_artifact):
            max_area = area
            best_artifact = artifact_id

    print(best_artifact, max_area)

if __name__ == "__main__":
    find_largest_artifact()
