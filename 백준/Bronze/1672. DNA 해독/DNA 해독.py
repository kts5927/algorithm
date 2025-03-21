import sys
input = sys.stdin.readline
def sol():
    num = {'A': 0, 'G': 1, 'C': 2, 'T': 3}
    change = [[0, 2, 0, 1],
            [2, 1, 3, 0],
            [0, 3, 2, 1],
            [1, 0, 1, 3]]

    N = int(input())
    DNA = input().strip()
    now = num[DNA[-1]]
    for c in range(N - 2, -1, -1):
        now = change[num[DNA[c]]][now]

    print("AGCT"[now])
sol()