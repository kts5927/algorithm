def manage_dvd_stock():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    index = 0
    results = []
    
    while index < len(data):
        stock_code = data[index].strip()
        if stock_code == "#":
            break
        index += 1

        M, S = map(int, data[index].strip().split())
        index += 1

        T = int(data[index].strip())
        index += 1

        for _ in range(T):
            transaction = data[index].strip().split()
            action = transaction[0]
            amount = int(transaction[1])
            if action == "S":
                S = max(0, S - amount)
            elif action == "R":
                S = min(M, S + amount)
            index += 1
        
        results.append(f"{stock_code} {S}")
    
    for result in results:
        print(result)

# 함수 호출
manage_dvd_stock()
