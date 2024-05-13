lst = list(map(str,input().split('/')))

if int(lst[0]) + int(lst[2]) < int(lst[1]) or int(lst[1]) == 0:
    print('hasu')
else:
    print('gosu')