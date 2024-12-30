def solve_c1_group(c1, A_set):
    for x1 in A_set:
        x2 = c1 - x1
        if x2 not in A_set:
            continue
        for x3 in A_set:
            x4 = x3 + x1
            if x4 not in A_set:
                continue
            for x6 in A_set:
                for x7 in A_set:
                    x5 = x6 + x7
                    if x5 not in A_set:
                        continue
                    for x10 in A_set:
                        if x2 + x10 == x6:
                            return [x1, x2, x3, x4, x5, x6, x7, x10]
    return None


def solve_c2_group(c2, A_set):
    for x8 in A_set:
        for x9 in A_set:
            x11 = x8 + x9
            if x11 not in A_set:
                continue
            x12 = x9 + c2
            if x12 in A_set:
                return [x8, x9, x11, x12]
    return None


def solve_equations(n, c1, c2, A):
    A_set = set(A)
    c1_group = solve_c1_group(c1, A_set)
    c2_group = solve_c2_group(c2, A_set)

    if c1_group and c2_group:
        x1, x2, x3, x4, x5, x6, x7, x10 = c1_group
        x8, x9, x11, x12 = c2_group
        return [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12]
    return None


n, c1, c2 = map(int, input().split())
A = [int(input()) for _ in range(n)]

result = solve_equations(n, c1, c2, A)

if result:
    print("\n".join(map(str, result)))
