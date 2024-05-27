N = int(input())

ans = 0
list = []

for i in range(1,int(N**0.5+1)):
    if i == 1:
        ans += 1
    else:
        cal = i*i
        while cal <= N: 
            if cal not in list:
                ans += 1
                list.append(cal)
            else:
                break
            cal = cal*cal
print(ans)