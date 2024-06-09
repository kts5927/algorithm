import sys

input = sys.stdin.read
data = input().splitlines()

N, K = map(int, data[0].split())

count_dict = {}

for i in range(1, 3 * N + 1):
    string = data[i]
    if string in count_dict:
        count_dict[string] = (count_dict[string][0] + 1, i)
    else:
        count_dict[string] = (1, i)

sorted_items = sorted(count_dict.items(), key=lambda x: (-x[1][0], -x[1][1]))

for i in range(min(K, len(sorted_items))):
    print(sorted_items[i][0])
