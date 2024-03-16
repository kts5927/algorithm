def z_traverse(n, r, c):
    if n == 1:
        return 0 if (r, c) == (0, 0) else 1 if (r, c) == (0, 1) else 2 if (r, c) == (1, 0) else 3

    size = 2 ** (n - 1)
    quadrant = (r // size) * 2 + (c // size)

    if quadrant == 0:
        return z_traverse(n - 1, r, c)
    elif quadrant == 1:
        return size ** 2 + z_traverse(n - 1, r, c - size)
    elif quadrant == 2:
        return 2 * size ** 2 + z_traverse(n - 1, r - size, c)
    else:
        return 3 * size ** 2 + z_traverse(n - 1, r - size, c - size)

# 입력 받기
n, r, c = map(int, input().split())

# 함수 호출
print(z_traverse(n, r, c))