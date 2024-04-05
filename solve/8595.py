import sys
N = int(input())
lst = list(map(str,input().strip()))
count = ''
ans = 0

for i in lst:
    print(i)
    if '0'<= i <= '9':
        count+=i
    else:
        if count == '':
            continue
        else:
            ans += int(count)
            count = ''

if count != '':
    ans += int(count)
print(ans)