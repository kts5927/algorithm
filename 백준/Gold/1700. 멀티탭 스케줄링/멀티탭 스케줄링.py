import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
socket = []
ans = 0

for i in range(K):
    if arr[i] in socket: 
        continue

    if len(socket) < N: 
        socket.append(arr[i])
    else:
        next_use = [arr[i:].index(s) if s in arr[i:] else K for s in socket]
        idx = next_use.index(max(next_use))
        socket[idx] = arr[i]
        ans += 1

print(ans)