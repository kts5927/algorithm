def dragoncurve(x,y,d,g):
    
    lst = [d]

    for j in range(g):
        a = len(lst)
        for k in range(a):
            lst.append((lst[a-k-1]+1)%4)
    table[y][x] = 1
    for k in lst:
        if k == 0:
            x += 1
            table[y][x] = 1
        elif k == 1:
            y -= 1
            table[y][x] = 1
        elif k == 2:
            x -= 1
            table[y][x] = 1
        elif k == 3:
            y += 1
            table[y][x] = 1
    
    

table = [[0]*101 for _ in range(101)]

N = int(input())
for i in range(N):
    x,y,d,g = map(int,input().split())
    dragoncurve(x,y,d,g)

ans = 0
for i in range(len(table)-1):
    for j in range(len(table[0])-1):
        if table[i][j] == 1 and table[i+1][j] == 1 and table[i][j+1] == 1 and table[i+1][j+1] == 1 :
            ans += 1
print(ans)