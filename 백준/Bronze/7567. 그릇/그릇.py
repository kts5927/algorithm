lst = list(map(str,input()))
lst.append('')

count = 0
switch = lst[0]
ans = 0
for i in lst:
    if i != switch:
        ans += 10 + (count-1)*5
        count = 1
        switch = i

    else:
        count += 1
        
print(ans)