import sys

N = int(sys.stdin.readline())
Hash = {}

for i in range(N):
    lst = list(map(int,sys.stdin.readline().split()))
    for i in lst:
        if i in Hash:
            print(1)
            exit(0)
        else:
            Hash[i] = 1

print(0)