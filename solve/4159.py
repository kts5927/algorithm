while True:
    N = int(input())
    if N == 0:
        break
    lst = [0]*N
    for _ in range(N):
        n = int(input())
        lst[_] = n
    
    lst.sort()
    if lst[0] > 200 or lst[-1] < 1322:
        print('IMPOSSIBLE')
        continue
    for i in range(1,N):
        if lst[i] - lst[i-1] > 200:
            print('IMPOSSIBLE')
            continue
        
    print('POSSIBLE')
    
    
    