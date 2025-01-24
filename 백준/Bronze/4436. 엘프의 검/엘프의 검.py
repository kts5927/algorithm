while True:
    try:
        N = int(input())
        lst = [False for i in range(10)]
        cal = 0
        K = 0
        while False in lst:
            cal += N
            K += 1
            num = list(map(str,str(cal).strip()))
            for i in num:
                lst[int(i)] = True
                
        print(K)
    except EOFError:
        break