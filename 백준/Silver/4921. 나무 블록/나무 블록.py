import sys

input = sys.stdin.readline

block_rules = {
    1: {4, 5},
    3: {4, 5},
    4: {2, 3},
    5: {8},
    6: {2, 3},
    7: {8},
    8: {6, 7}
}

num = 0

while True:
    N = input().strip()
    if N == "0":
        break

    num += 1
    blocks = list(N)

    if blocks[0] != '1':
        print(f"{num}. NOT")
        continue

    valid = True
    for i in range(len(blocks) - 1):
        if int(blocks[i+1]) not in block_rules.get(int(blocks[i]), set()):
            valid = False
            break

    if valid and blocks[-1] != '2':
        valid = False

    print(f"{num}. {'VALID' if valid else 'NOT'}")
