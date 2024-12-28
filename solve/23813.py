num = list(map(str,input().strip()))

ans = 0
for i in range(len(num)):
    num.insert(0,num.pop())
    ans += int("".join(num))
    
print(ans)