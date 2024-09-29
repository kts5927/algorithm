lst = [[0]*1001 for _ in range(1001)]

N = int(input())
for k in range(N):
    a,b,c,d = map(int,input().split())
    
    for i in range(c):
        for j in range(d):
            lst[i+a][j+b] = k+1


ans = [0]*1002
for i in range(1001):
    for j in range(1001):
        ans[lst[i][j]] += 1
        
for i in range(N):
    print(ans[i+1])