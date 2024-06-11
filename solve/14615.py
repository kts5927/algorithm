from collections import deque
import sys

input = sys.stdin.readline

def BFS(start, lst):
    deq = deque([start])
    visited = [False] * (N + 1)
    visited[start] = True
    while deq:
        numb = deq.popleft()
        for i in lst[numb]:
            if not visited[i]:
                visited[i] = True
                deq.append(i)
    return visited

N, M = map(int, input().split())
forward = [[] for _ in range(N + 1)]
reverse = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    forward[a].append(b)
    reverse[b].append(a)

first = BFS(1, forward)
second = BFS(N, reverse)

T = int(input())
for _ in range(T):
    n = int(input())
    if first[n] and second[n]:
        print('Defend the CTP')
    else:
        print('Destroyed the CTP')

