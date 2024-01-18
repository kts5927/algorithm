import sys
sys.setrecursionlimit(10**7)
n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
field = [[0 for j in range(n)] for i in range(n)]

a = max(max(row) for row in table)

def field_ready(k: int):
    for i in range(n):
        for j in range(n):
            if table[i][j] > k:
                field[i][j] = 1

def field_clear():
    for i in range(n):
        for j in range(n):
            field[i][j] = 0

def security(n: int, t: int):
    security_count = 0
    field_ready(n)
    for i in range(t):
        for j in range(t):
            if field[i][j] == 1:
                check(i, j)
                security_count += 1

    field_clear()
    return security_count

def solve(max_value: int):
    answer = []
    for i in range(max_value):
        x = security(i, n)
        answer.append(x)
    print(max(answer))

def check(i: int, j: int):
    field[i][j] = 0
    if i < n - 1 and field[i + 1][j] != 0:
        check(i + 1, j)
    if j < n - 1 and field[i][j + 1] != 0:
        check(i, j + 1)
    if i > 0 and field[i - 1][j] != 0:
        check(i - 1, j)
    if j > 0 and field[i][j - 1] != 0:
        check(i, j - 1)


solve(a)