N,M = map(int,input().split())

LR = [[0,N]]
UD = [[0,M]]

T = int(input())
for i in range(T):
    LRUD, point = map(int,input().split())
    if LRUD == 0:
        for i in range(len(UD)):
            if UD[i][0] < point < UD[i][1]:
                UD.append([UD[i][0],point])
                UD.append([point,UD[i][1]])
                UD.remove(UD[i])
    else:
        for i in range(len(LR)):
            if LR[i][0] < point < LR[i][1]:
                LR.append([LR[i][0],point])
                LR.append([point,LR[i][1]])
                LR.remove(LR[i])


ans = 0
for i in LR:
    for j in UD:
        ans = max(ans,(i[1]-i[0])*(j[1]-j[0]))
        
        
print(ans)