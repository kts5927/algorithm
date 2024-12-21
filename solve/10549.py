import sys

T = int(sys.stdin.readline())
Hash = {}
for i in range(T):
    name = str(sys.stdin.readline())
    if name in Hash:
        Hash[name] += 1
    else:
        Hash[name] = 1    
for i in range(T-1):
    name = str(sys.stdin.readline())
    Hash[name] -= 1
    
for i in Hash:
    if Hash[i] != 0:
        print(i)