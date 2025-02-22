code = {
    "063": 0,
    "010": 1,
    "093": 2,
    "079": 3,
    "106": 4,
    "103": 5,
    "119": 6,
    "011": 7,
    "127": 8,
    "107": 9,
}

code_rev = {v: k for k, v in code.items()}


def num(m):
    n = ""
    for i in range(0, len(m), 3):
        n += str(code[m[i : i + 3]])
    return int(n)


while True:
    q = input()
    if q == 'BYE':
        break

    a, b = q.split('+')
    a_num = num(a)
    b_num = num(b[:-1])
    sum_num = str(a_num + b_num)

    ans = ''
    for i in sum_num:
        ans += code_rev[int(i)]

    print(q + ans)
