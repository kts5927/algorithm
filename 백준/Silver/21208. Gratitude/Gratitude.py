import sys

input = sys.stdin.read
data = input().splitlines()

N, K = map(int, data[0].split())

hash_table = {}

for i in range(1, 3 * N + 1):
    string = data[i]
    if string in hash_table:
        hash_table[string] = (hash_table[string][0] + 1, i)
    else:
        hash_table[string] = (1, i)

ans = sorted(hash_table.items(), key=lambda x: (-x[1][0], -x[1][1]))

for i in range(min(K, len(ans))):
    print(ans[i][0])
