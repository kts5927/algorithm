import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

def next_permutation(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    
    if i == -1:
        return False
    
    j = len(arr) - 1
    while arr[i] >= arr[j]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])
    return True

if next_permutation(lst):
    print(' '.join(map(str, lst)))
else:
    print(-1)
