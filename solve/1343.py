import sys
lst = list(map(str,sys.stdin.readline().strip()))

if 'X' not in lst:
    print(''.join(lst))
else:

    cnt = []
    count = 0
    for i in lst:
        if i == '.':
            if count != 0:
                cnt.append(count)
            cnt.append(-1)
            count = 0
        else:
            count+= 1
    if count != 0:
        cnt.append(count)
        
    ans = []
    for i in cnt:
        while i > 0:
            if i == 1 or i == 3:
                ans = -1
                break
            elif i>=4:
                i -= 4
                ans.append('AAAA')
            elif i>=2:
                i -= 2
                ans.append('BB')
        if i == -1:
            ans.append('.')
        if ans == -1:
            break
        
        
    if ans != -1:
        print(''.join(ans))
    else:
        print(ans)
