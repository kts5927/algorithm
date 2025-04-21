from collections import Counter

while True:
    try:
        a = input()
        b = input()

        count_a = Counter(a)
        count_b = Counter(b)

        result = []

        for ch in 'abcdefghijklmnopqrstuvwxyz':
            common = min(count_a[ch], count_b[ch])
            result.extend([ch] * common)

        print(''.join(result))
    except EOFError:
        break
