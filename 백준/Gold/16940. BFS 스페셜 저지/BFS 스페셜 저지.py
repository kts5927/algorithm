import sys
from collections import deque

def fail():
    print(0)
    sys.exit()

N = int(sys.stdin.readline())
Node = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    Node[a].append(b)
    Node[b].append(a)

lst = list(map(int, sys.stdin.readline().split()))
numb = [0] * N
distance = [0] * (N + 1)
child = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
visited[1] = 1

que = deque()
que.append((lst[0], 0))
while que:
    location, dist = que.popleft()
    numb[dist] += 1
    distance[location] = dist
    for i in Node[location]:
        if visited[i] == 0:
            que.append((i, dist + 1))
            child[location].append(i)
            visited[i] = 1

visited = [0] * (N + 1)
visited[1] = 1
pointer = 1

for i in lst:
    if numb[distance[i]] > 0:
        numb[distance[i]] -= 1
    else:
        fail()

    current_child_list = sorted(lst[pointer:pointer + len(child[i])])
    expected_child_list = sorted(child[i])

    if current_child_list != expected_child_list:
        fail()
    
    pointer += len(child[i])

print(1)
