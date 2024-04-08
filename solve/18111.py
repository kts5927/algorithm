N,M,B = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]


min_ = lst[0][0]
max_ = 0
for i in range(N):
    for j in range(M):
        if lst[i][j] > max_:
            max_ = lst[i][j]
        elif lst[i][j] < min_:
            min_ = lst[i][j]
      
land = min_      
ans1 = float('inf')
ans2 = 0
while land <= max_:
    count = 0
    block = B
    for i in range(N):
        for j in range(M):
            if lst[i][j] > land:
                count += (lst[i][j] - land)*2
                block += lst[i][j] - land
            elif lst[i][j] < land:
                block -= land-lst[i][j]
                count += land - lst[i][j]
    if block >= 0 and count <= ans1:
        ans1 = count
        if ans2 < land:
            ans2 = land
    else : 
        break
    
    land += 1
print(ans1,ans2)
