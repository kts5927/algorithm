normal = list(str(input()))
compare = list(str(input()))

passwordkey = compare*(len(normal) // len(compare) + 1)
ans = []
for i in range(len(normal)):
    if normal[i] == ' ':
        ans.append(' ')
    else:

        cal = (ord(normal[i]))-ord(passwordkey[i])+96
        if cal < 97:
            cal += 26
        ans.append(chr(cal))
print(''.join(ans))
        