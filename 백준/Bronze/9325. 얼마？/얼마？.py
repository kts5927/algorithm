import sys
readline=sys.stdin.readline
T=int(readline())
for _ in range(T):
    s=int(readline())
    n=int(readline())
    for __ in range(n):
        q,p=map(int,readline().split())
        s+=q*p
    print(s)
