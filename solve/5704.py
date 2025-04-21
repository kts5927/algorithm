while True:
    S = list(map(str,input().strip()))
    if S == ['*']:
        break
    unicord = [0 for _ in range(26)]
    
    for i in S:
        if i != ' ':
            unicord[ord(i)-ord('a')] = 1
    
    if sum(unicord) == 26:
        print('Y')
    else:
        print('N')