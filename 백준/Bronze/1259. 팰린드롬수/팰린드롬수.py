while True:
    a = list(map(int,input().strip()))
    if a == [0]:
        break
    b = list(reversed(a))
    if a == b :
        print('yes')
    else : print('no')