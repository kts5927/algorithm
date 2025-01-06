KICKS = list(map(str,input().strip()))
KICK = ['k','i','c','k']
ans = 0
for i in range(len(KICKS)-3):
    if KICKS[i] == 'k':
        flag = 1
        for j in range(4):
            if KICKS[i+j] != KICK[j]:
                flag = 0
                break
        if flag:
            ans += 1
        
print(ans)