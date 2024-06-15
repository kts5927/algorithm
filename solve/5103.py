import sys
while True:
    stock_code = sys.stdin.readline().rstrip()
    if stock_code == '#':
        break
    M, S = map(int, sys.stdin.readline().split())
    T = int(sys.stdin.readline())
    for _ in range(T):
        a, b = map(str, sys.stdin.readline().split())
        b = int(b)
        if a == 'S':
            S -= b
            if S < 0:
                S = 0
        elif a == 'R':
            S += b
            if S > M:
                S = M
    ans = [stock_code, S]
    print(*ans)
