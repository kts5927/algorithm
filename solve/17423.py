lst = list(map(str,input().strip()))

buff = []
ans = []
switch = True
for i in lst:
    if i == ' ':
        if switch:
            while buff:
                ans.append(buff.pop())
            ans.append(i)
        else:
            buff.append(i)
    elif i == '<':
        while buff:
            ans.append(buff.pop())
        switch = False
        buff.append(i)
    elif i == '>':
        buff.append('>')
        switch = True
        for j in buff:
            ans.append(j)
            buff = []
    else:
        buff.append(i)
if buff:
    while buff:
        ans.append(buff.pop())
print(''.join(ans))