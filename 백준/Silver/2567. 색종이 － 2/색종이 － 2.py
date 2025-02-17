table = [[0 for _ in range(102)] for _ in range(102)]

T = int(input())
for _ in range(T):
    l,r = map(int,input().split())
    
    for i in range(l,l+10):
        for j in range(r,r+10):
            table[i][j] = 1
            
ans = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(101):
    for j in range(101):
        if table[i][j] == 1:
            if table[i-1][j] == 0:
                ans += 1
            if table[i][j-1] == 0:
                ans += 1
            if table[i+1][j] == 0:
                ans += 1
            if table[i][j+1] == 0:
                ans += 1
print(ans)