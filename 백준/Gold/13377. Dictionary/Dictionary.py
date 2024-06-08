from itertools import permutations

alphabet = ['a','b','c','d','e','f','g','h','i']
lst = list(permutations(alphabet,9))
for i in range(362880):
    lst[i] = ''.join(lst[i])
    
N = int(input())
for i in range(N):
    string = input()
    print(lst.index(string)+1)
