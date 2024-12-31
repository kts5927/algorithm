import sys
n = int(sys.stdin.readline())
bomb = [int(sys.stdin.readline()) for _ in range(n)]
if n==1:
    print(1)
else:
    if bomb[0]>=bomb[1]:
        print(1)
    for i in range(1,n-1):
        if bomb[i - 1] <= bomb[i] and bomb[i] >= bomb[i + 1]:
            print(i + 1)
    if bomb[n-2]<=bomb[n-1]:
        print(n)