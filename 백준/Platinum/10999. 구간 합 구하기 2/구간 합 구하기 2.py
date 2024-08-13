import sys
import math
input = sys.stdin.readline


def get_tree_length():
    if N & (N-1) == 0:
        return 2*N
    else:
        return pow(2, math.ceil(math.log(N, 2)) + 1)


def initialize(index, start, end):
    if start == end:
        segment[index] = nums[start]
        return

    mid = (start + end)//2
    initialize(index*2, start, mid)
    initialize(index*2+1, mid+1, end)
    segment[index] = segment[index*2] + segment[index*2+1]


def update(index, start, end, left, right, to_added):
    prograte(index, start, end)

    if right < start or end < left:
        return

    if left <= start and end <= right:
        segment[index] += (end - start + 1)*to_added

        if start != end:
            lazy[index*2] += to_added
            lazy[index*2+1] += to_added

        return

    mid = (start + end)//2
    update(index*2, start, mid, left, right, to_added)
    update(index*2+1, mid+1, end, left, right, to_added)
    segment[index] = segment[index*2] + segment[index*2+1]


def query(index, start, end, left, right):
    prograte(index, start, end)

    if right < start or end < left:
        return 0

    if left <= start and end <= right:
        return segment[index]

    mid = (start + end)//2
    return query(index*2, start, mid, left, right) + query(index*2+1, mid+1, end, left, right)


def prograte(index, start, end):
    if lazy[index] != 0:
        segment[index] += (end - start + 1)*lazy[index]

        if start != end:
            lazy[index*2] += lazy[index]
            lazy[index*2+1] += lazy[index]

        lazy[index] = 0


if __name__ == '__main__':
    N, M, K = map(int, input().split())

    nums = [-1] + [int(input()) for _ in range(N)]

    tree_length = get_tree_length()
    segment = [0]*tree_length
    lazy = [0]*tree_length
    initialize(1, 1, N)

    for _ in range(M+K):
        cur = list(map(int, input().split()))

        if cur[0] == 1:
            _, b, c, d = map(int, cur)
            update(1, 1, N, b, c, d)

        else:
            _, b, c = map(int, cur)
            print(query(1, 1, N, b, c))
