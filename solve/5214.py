import sys
from collections import deque

N, K, M = map(int, sys.stdin.readline().split())

station_to_tubes = [[] for _ in range(N + 1)]
tube_to_stations = [[] for _ in range(M + 1)]

for i in range(1, M + 1):
    lst = list(map(int, sys.stdin.readline().split()))
    for j in lst:
        station_to_tubes[j].append(i)
        tube_to_stations[i].append(j)

visited_stations = [False] * (N + 1)
visited_tubes = [False] * (M + 1)
que = deque()
que.append((1, 1))  
visited_stations[1] = True

while que:
    current_station, count = que.popleft()

    if current_station == N:
        print(count)
        sys.exit(0)

    for tube in station_to_tubes[current_station]:
        if not visited_tubes[tube]:
            visited_tubes[tube] = True
            for next_station in tube_to_stations[tube]:
                if not visited_stations[next_station]:
                    visited_stations[next_station] = True
                    que.append((next_station, count + 1))

print(-1)
