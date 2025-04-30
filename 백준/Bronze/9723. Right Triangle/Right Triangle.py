import sys
input = sys.stdin.readline

T = int(input())
for t in range(1, T + 1):
    a, b, c = sorted(map(int, input().split()))
    if a**2 + b**2 == c**2:
        print(f"Case #{t}: YES")
    else:
        print(f"Case #{t}: NO")
