import sys
input = sys.stdin.readline


Quest_TABLE = [[False for _ in range(25)] for _ in range(25)]
AP = [[0 for _ in range(25)] for _ in range(25)]
Quest_STR = []
Quest_INT = []
Quest_PNT = []
T = int(input())

for _ in range(T):
    STR,INT,PNT = map(int,input().split())
    Quest_STR.append(STR)
    Quest_INT.append(INT)
    Quest_PNT.append(PNT)
    
ans = 0
for STR in range(1,25):
    for INT in range(1,25):
        AP[STR][INT] = 2-STR-INT
        
        count = 0
        
        for i in range(T):
            if Quest_STR[i] <= STR or Quest_INT[i] <= INT:
                AP[STR][INT] += Quest_PNT[i]
                count += 1
                
        if ((STR == 1 and INT == 1) 
            or (STR > 1 and Quest_TABLE[STR-1][INT] and AP[STR-1][INT] > 0) 
            or (INT > 1 and Quest_TABLE[STR][INT-1] and AP[STR][INT-1] > 0)):
            
            Quest_TABLE[STR][INT] = True
        
        if Quest_TABLE[STR][INT]:
            ans = max(ans,count)

print(ans)
        
        
