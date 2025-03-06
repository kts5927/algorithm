from itertools import product

N = int(input())
S = input()

binary_numbers = [''.join(bits) for bits in product('01', repeat=N)]

binary_numbers.sort(key=lambda x: (x.count('1'), int(x[::-1], 2)))

print(binary_numbers.index(S))
