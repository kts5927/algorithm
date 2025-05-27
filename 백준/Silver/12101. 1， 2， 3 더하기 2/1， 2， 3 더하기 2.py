import sys
sys.setrecursionlimit(10000)

n, k = map(int, input().split())
count = 0
found = False

def dfs(current_sum, path):
    global count, found
    if found:
        return
    if current_sum == n:
        count += 1
        if count == k:
            print('+'.join(map(str, path)))
            found = True
        return
    for i in [1, 2, 3]:
        if current_sum + i <= n:
            dfs(current_sum + i, path + [i])

dfs(0, [])
if not found:
    print(-1)
