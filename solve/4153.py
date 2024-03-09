while True:
    number = list(map(int,input().split()))
    if not number[0] and not number[1] and not number[2]:
        break
    
    a = max(number)
    number.remove(a)
    if a**2 == number[0]**2 + number[1]**2:
        print(*"right",sep='')
    else: print(*"wrong",sep='')