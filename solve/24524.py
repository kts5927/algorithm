S = list(map(str,input().strip()))
check = [False for _ in range(len(S))]
T = list(map(str,input().strip()))


ans = 0
for i in range(len(S)):
    if S[i] == T[0] and check[i] == False:
        check[i] = True
        Flag = False
        isans = 1
        for j in range(1,len(T)):
            
            Flag = False
            for k in range(i+1,len(S)):
                if S[k] == T[j] and check[k] == False:
                    isans += 1
                    check[k] = True
                    Flag = True
                    break
            if not Flag:
                print(ans)
                exit()
        if isans == len(T):
            ans += 1
print(ans)

