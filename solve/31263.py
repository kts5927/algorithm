N = int(input())
lst = list(map(str, input().strip()))

ans = 0
cal = 0

while lst:
    if len(lst) <= 3:
        if int(''.join(lst[:3])) <= 641:
            ans += 1
            break
        else:
            lst = lst[2:]
            ans += 1
    else:
        if lst[2] == '0':
            
            if lst[3] == '0':
                lst = lst[1:]
                ans += 1
            else:
                if int(''.join(lst[:3])) <= 641:
                    lst = lst[3:]
                    ans += 1
                else:
                    lst = lst[1:]
                    ans += 1

        else:
            if lst[3] == '0':
                lst = lst[2:]
                ans += 1
            else:
                if int(''.join(lst[:3])) <= 641:
                    lst = lst[3:]
                    ans += 1
                else:
                    lst = lst[2:]
                    ans += 1
         
print(ans)

