import sys

N = int(sys.stdin.readline())
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if a % 10 == 0:
        print(10) 
    else:
        b = (b % 4) + 4
        print((a ** b) % 10)