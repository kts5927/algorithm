D = int(input())
campus = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0],
]

def multiplication(a, b):
    temp = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            for k in range(8):
                temp[i][j] += a[i][k] * b[k][j]
            temp[i][j] %= 1000000007

    for i in range(8):
        for j in range(8):
            a[i][j] = temp[i][j]

ans = [[0] * 8 for _ in range(8)]
for i in range(8):
    ans[i][i] = 1

while D > 0:
    if D % 2 != 0:
        multiplication(ans, campus)
    multiplication(campus, campus)
    D //= 2

print(ans[0][0])