lst = [0]*5
Str = str(input().strip())

for i in Str:
    if i == 'M':
        lst[0] = 1
    elif i == 'O':
        lst[1] = 1
    elif i == 'B':
        lst[2] = 1
    elif i == 'I':
        lst[3] = 1
    elif i == 'S':
        lst[4] = 1
    
if sum(lst) == 5:
    print('YES')
else:
    print('NO')