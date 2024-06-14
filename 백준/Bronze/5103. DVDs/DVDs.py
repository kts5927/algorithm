import sys

while True:
    # 재고 코드를 입력 받습니다.
    stock_code = sys.stdin.readline().rstrip()
    if stock_code == '#':
        break
    
    # 최대 재고(M)와 현재 재고(S)를 입력 받습니다.
    M, S = map(int, sys.stdin.readline().split())
    
    # 거래 횟수(T)를 입력 받습니다.
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        # 각 거래를 입력 받습니다.
        a, b = map(str, sys.stdin.readline().split())
        b = int(b)
        
        if a == 'S':
            # 판매인 경우
            S -= b
            if S < 0:
                S = 0
        elif a == 'R':
            # 재고인 경우
            S += b
            if S > M:
                S = M
    
    # 최종 결과를 출력합니다.
    ans = [stock_code, S]
    print(*ans)
