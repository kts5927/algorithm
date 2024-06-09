from itertools import permutations
import sys

alphabet = ['a','b','c','d','e','f','g','h','i']
lst = list(permutations(alphabet,9))
for i in range(362880):
    lst[i] = ''.join(lst[i])

check = {}
i = 1
for w in lst:
    check[w] = i
    i += 1
    
N = int(sys.stdin.readline())
for i in range(N):
    string = sys.stdin.readline().strip()
    print(check[string])
