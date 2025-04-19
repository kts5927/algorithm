import sys

value = {
    '-': 0,
    '\\': 1,
    '(': 2,
    '@': 3,
    '?': 4,
    '>': 5,
    '&': 6,
    '%': 7,
    '/': -1,
}

for line in sys.stdin:
    s = line.rstrip()
    if s == '#':
        break
    num = 0
    for ch in s:
        num = num * 8 + value[ch]
    print(num)

    